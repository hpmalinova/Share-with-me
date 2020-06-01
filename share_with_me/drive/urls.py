from django.urls import path, include

from drive.views import index, images

app_name = 'drive'

images_patterns = [
    # NEW
    path('', images.base, name='base'),
    path('courses/<int:course_id>/<str:spec>/<str:subj>/list', images.list, name='list'),
    # path('new/', images.ImageCreateView.as_view(), name='create'),
    path('courses/', images.courses, name='courses'),
    # NO speciality or subject
    path('courses/<int:course_id>', images.speciality, name='speciality'),
    path('courses/<int:course_id>/<str:spec>/', images.subject, name='subject'),
    path('courses/<int:course_id>/<str:spec>/<str:subj>/', images.detail_subject,
         name='detail_subject'),
    path('courses/<int:course_id>/<str:spec>/<str:subj>/upload',
         images.upload_file,
         name='upload_file'),
    # MOVED
    path('courses/<int:course_id>/<str:spec>/<str:subj>/<int:image_id>/', images.detail, name='detail')
    # path('new-experiment/', images.new_experiment, name='new-experiment'),
    # path('update/<int:course_id>/', images.edit_course, name='update'),
    # path('delete/<int:course_id>/', images.delete_course, name='delete'),
    # path('session/', images.session, name='session'),
]

urlpatterns = [
    path('', index, name='index'),
    path('drive/', include((images_patterns, 'images')))
]
