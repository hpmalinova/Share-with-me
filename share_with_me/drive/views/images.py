from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from drive.models import Image, Courses

from django import forms
from django.http import HttpResponse


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
            'courses': Courses.objects.values_list('course', flat=True).distinct().order_by('course')
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
            'course': Courses.objects.filter(course=course, specialty=specialty, subject=subject).first(),
        }
    )


def upload_file(request, path):
    if request.method == "POST":
        flag = False
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'image/' in str(request.FILES):
                instance.image = instance.file
                flag = True
            course = Courses.objects.filter(path=path).first()
            instance.course_path = course
            instance.save()
            if flag is True:
                instance.file = None
                instance.save(update_fields=['file'])
            return redirect(reverse('drive:images:list',
                                    args=[path, ]))
        else:
            return render(
                request,
                'images/upload_file.html',
                {
                    'form': form,
                    'path': path,
                }
            )
    else:
        form = ImageForm()
        return render(
            request,
            'images/upload_file.html',
            {
                'form': form,
                'path': path,
            }
        )


def list(request, path):
    course = Courses.objects.filter(path=path).first()
    return render(
        request,
        'images/list.html',
        {
            'course': course,
            'path': path,
            'images': Image.objects.filter(course_path=path)
        }
    )


def detail(request, path, image_id):
    image = get_object_or_404(Image, id=image_id)

    return render(
        request,
        'images/detail.html',
        {
            'path': path,
            'image': image,
        }
    )


def search(request):
    print(request.path)
    if 'q' in request.GET:
        message = request.GET['q']
        courses = Courses.objects.filter(subject__contains=message)
        return render(
            request,
            'images/search.html',
            {
                'courses': courses
            }
        )
    else:
        message = "You submitted an empty form."
    return HttpResponse(message)
