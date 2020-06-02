from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import CreateView
from django.urls import reverse
from drive.models import Image, Courses

from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'file',)


def base(request):
    return render(
        request,
        'images/base.html',
    )


def courses(request):
    return render(
        request,
        'images/courses.html',
        {
            'courses': Courses.objects.values_list('course', flat=True).distinct()
        }
    )


def speciality(request, course):
    return render(
        request,
        'images/speciality.html',
        {
            'course': course,
            'specialties': Courses.objects.values_list('specialty', flat=True).filter(course=course).distinct()
        }
    )


def subject(request, course, specialty):
    return render(
        request,
        'images/subject.html',
        {
            'course': course,
            'specialty': specialty,
            'subjects': Courses.objects.values_list('subject', flat=True).filter(course=course, specialty=specialty)
        }
    )


def detail_subject(request, course, specialty, subject):
    return render(
        request,
        'images/detail_subject.html',
        {
            'course': course,
            'specialty': specialty,
            'subject': subject,
            'path': Courses.objects.filter(course=course, specialty=specialty, subject=subject).first().path
        }
    )


def upload_file(request, course, specialty, subject):
    if request.method == "POST":
        flag = False
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'image/' in str(request.FILES):
                instance.image = instance.file
                flag = True
            instance.course_path = Courses(
                course=course,
                specialty=specialty,
                subject=subject,
                path=f'{course}/{specialty}/{subject}'
            )
            instance.save()

            if flag is True:
                instance.file = None
                instance.save(update_fields=['file'])
            return redirect(reverse('drive:images:detail_subject', args=[course, specialty, subject]))

        else:
            return render(
                request,
                'images/upload_file.html',
                {
                    'form': form,
                    'course': course,
                    'specialty': specialty,
                    'subject': subject,
                }
            )
    else:
        form = ImageForm()
        return render(
            request,
            'images/upload_file.html',
            {
                'form': form,
                'course': course,
                'specialty': specialty,
                'subject': subject,
            }
        )


def list(request, course, specialty, subject):
    path = f'{course}/{specialty}/{subject}'

    return render(
        request,
        'images/list.html',
        {
            'course': course,
            'specialty': specialty,
            'subject': subject,
            'images': Image.objects.filter(course_path=path)
        }
    )


def detail(request, course, specialty, subject, image_id):
    image = get_object_or_404(Image, id=image_id)

    return render(
        request,
        'images/detail.html',
        {
            'course': course,
            'specialty': specialty,
            'subject': subject,
            'image': image,
        }
    )
