from django.shortcuts import render
from drive.models import Courses, Image


def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # values_list('course', flat=True).distinct().
    num_subjects = Courses.objects.all().count()
    num_files = Image.objects.all().count()

    context = {
        'num_subjects': num_subjects,
        'num_files': num_files,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

import drive.views.images
