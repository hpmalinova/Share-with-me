from django.urls import path, include

from drive.views import index, images

app_name = 'drive'

images_patterns = [
    path('', images.list, name='list'),
    path('<int:image_id>/', images.detail, name='detail'),
    path('new/', images.ImageCreateView.as_view(), name='create'),
    path('courses/', images.courses, name='courses'),
    path('courses/<int:course_id>/speciality/', images.speciality, name='speciality'),
    path('courses/<int:course_id>/speciality/<str:spec>/subject/', images.subject, name='subject'),
    path(
        'courses/<int:course_id>/speciality/<str:spec>/subject/<str:subj>/upload',
        images.spec_subject,
        name='spec_subject'
    ),
    # path('new-experiment/', images.new_experiment, name='new-experiment'),
    # path('update/<int:course_id>/', images.edit_course, name='update'),
    # path('delete/<int:course_id>/', images.delete_course, name='delete'),
    # path('session/', images.session, name='session'),
]

urlpatterns = [
    path('', index, name='index'),
    path('drive/', include((images_patterns, 'images')))
]
