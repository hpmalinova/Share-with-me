from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse

from drive.models import Image, content_file_name

from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'file', 'description')


def spec_subject(request, course_id, spec, subj):
    if request.method == "POST":
        # print(request.get_full_path())
        data = request.POST
        form = ImageForm(data=data)
        print(form)
        if form.is_valid():
            print('HEREHEREHEREHEREHEREHERE')
            new_image = form.save(commit=True)
            return redirect(reverse('drive:images:list'))
        else:
            print('THERETHERETHERETHERETHERE')
            return render(
                request,
                'images/spec_subject.html',
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
            'images/spec_subject.html',
            {
                'form': form,
                'course_id': course_id,
                'spec': spec,
                'subj': subj
            }
        )
    '''
    return render(
        request,
        'images/spec_subject.html',
        {
            'course_id': course_id,
            'spec': spec,
            'subj': subj
        }
    )
    '''


# TODO: Make dictionaries of the subjects for each year and speciality
def subject(request, course_id, spec):
    return render(
        request,
        'images/subject.html',
        {
            'subjects': ['Math1', 'Math2'],
            'course_id': course_id,
            'spec': spec
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


def list(request):
    return render(
        request,
        'images/list.html',
        {
            'images': Image.objects.all()
        }
    )


def detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    return render(
        request,
        'images/detail.html',
        {
            'image': image
        }
    )


class ImageCreateView(CreateView):
    model = Image
    fields = ['description', 'image', 'file']
    template_name = 'images/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('drive:images:detail', kwargs={'image_id': self.object.id})
