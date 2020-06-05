from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from drive.models import Image, Courses, Comments

from django import forms
from django.db.models import Q
# from django.http import HttpResponse


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'file',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('username', 'comment', 'rating')


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


def specialty(request, course):
    return render(
        request,
        'images/specialty.html',
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
    comments = Comments.objects.filter(file=image)
    return render(
        request,
        'images/detail.html',
        {
            'path': path,
            'image': image,
            'comments': comments,
        }
    )


def search(request):
    something_found = False
    if request.GET.get('q'):
        message = request.GET['q']
        found_subjects = Courses.objects.filter(subject__contains=message)
        found_specialties = Courses.objects.values_list('course', 'specialty')\
                                           .filter(specialty__contains=message)\
                                           .distinct().order_by('course')
        found_files = Image.objects.filter(Q(image__contains=message) | Q(file__contains=message))
        if found_subjects or found_specialties or found_files:
            something_found = True

        return render(
            request,
            'images/search.html',
            {
                'something_found': something_found,
                'found_subjects': found_subjects,
                'found_specialties': found_specialties,
                'found_files': found_files,
            }
        )
    else:
        message = "You submitted an empty form."
        return render(
            request,
            'images/search.html',
            {
                'something_found': something_found,
            }
        )


def add_comment(request, path, image_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        file = Image.objects.filter(id=image_id).first()

        if form.is_valid() and file:
            instance = form.save(commit=False)
            instance.file = file
            instance.save()
            return redirect(reverse('drive:images:detail',
                                    args=[path, image_id]))
        else:
            return render(
                request,
                'images/add_comment.html',
                {
                    'form': form,
                    'path': path,
                    'image_id': image_id,
                }
            )
    else:
        form = CommentForm()
        return render(
            request,
            'images/add_comment.html',
            {
                'form': form,
                'path': path,
                'image_id': image_id,
            }
        )


def about(request):
    return render(
        request,
        'images/about.html',
    )
