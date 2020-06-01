from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from drive.models import Image

from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'file',)


def upload_file(request, course_id, spec, subj):
    if request.method == "POST":
        flag = False
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if 'image/' in str(request.FILES):
                instance.image = instance.file
                flag = True

            instance.course = course_id
            instance.speciality = spec
            instance.subject = subj
            instance.save()

            if flag is True:
                instance.file = None
                instance.save(update_fields=['file'])
            return redirect(reverse('drive:images:detail_subject', args=[course_id, spec, subj]))
        else:
            return render(
                request,
                'images/upload_file.html',
                {
                    'form': form,
                    'course_id': course_id,
                    'spec': spec,
                    'subj': subj
                }
            )
    else:
        form = ImageForm()
        return render(
            request,
            'images/upload_file.html',
            {
                'form': form,
                'course_id': course_id,
                'spec': spec,
                'subj': subj
            }
        )


# TODO: Make dictionaries of the subjects for each year and speciality
def subject(request, course_id, spec):
    return render(
        request,
        'images/subject.html',
        {
            'subjects': ['Algebra1', 'Algebra2'],
            'course_id': course_id,
            'spec': spec
        }
    )


def detail_subject(request, course_id, spec, subj):
    return render(
        request,
        'images/detail_subject.html',
        {
            'course_id': course_id,
            'spec': spec,
            'subj': subj,
            'images': Image.objects.filter(speciality=spec, subject=subj,
                                           course=course_id)
        }
    )


def speciality(request, course_id):
    return render(
        request,
        'images/speciality.html',
        {
            'course_id': course_id
        }
    )


def courses(request):
    return render(
        request,
        'images/courses.html'
    )


def list(request, course_id, spec, subj):
    return render(
        request,
        'images/list.html',
        {
            'course_id': course_id,
            'spec': spec,
            'subj': subj,
            'images': Image.objects.filter(speciality=spec, subject=subj,
                                           course=course_id)
        }
    )


def base(request):
    return render(
        request,
        'images/base.html',
        {
            # 'images': Image.objects.all()
        }
    )


def detail(request, course_id, spec, subj, image_id):
    image = get_object_or_404(Image, id=image_id)

    return render(
        request,
        'images/detail.html',
        {
            'course_id': course_id,
            'spec': spec,
            'subj': subj,
            'image': image,
        }
    )


# class ImageCreateView(CreateView):
#     model = Image
#     fields = ['description', 'image', 'file']
#     template_name = 'images/create.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('drive:images:detail', kwargs={'image_id': self.object.id})
