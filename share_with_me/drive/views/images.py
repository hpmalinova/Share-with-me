from django.shortcuts import render, get_object_or_404
# from django.views.generic import CreateView
# from django.urls import reverse_lazy

from drive.models import Image


def list(request):
    return render(request, 'images/list.html', {'images': Image.objects.all()})


def detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'images/detail.html', {'image': image})


# class ImageCreateView(CreateView):
#     model = Course
#     fields = ['name', 'description', 'start_date', 'end_date']
#     template_name = 'courses/create.html'

#     def get_success_url(self, **kwargs):
#         return reverse_lazy('education:courses:detail', kwargs={'course_id': self.object.id})