from django.urls import path, include

from drive.views import index, images

app_name = 'drive'

images_patterns = [
    path('', images.base, name='base'),
    path('courses/', images.courses, name='courses'),
    path('courses/<int:course>/', images.speciality, name='speciality'),
    path('courses/<int:course>/<str:specialty>/', images.subject, name='subject'),
    path('courses/<int:course>/<str:specialty>/<str:subject>/',
         images.detail_subject, name='detail_subject'),
    path('courses/<path:path>/upload', images.upload_file, name='upload_file'),
    # path('courses/<int:course>/<str:specialty>/<str:subject>/list', images.list, name='list'),
    path('courses/<path:path>/list/', images.list, name='list'),
    path('courses/<path:path>/<int:image_id>/', images.detail, name='detail'),
    path('search/', images.search, name='search')
]

urlpatterns = [
    path('', index, name='index'),
    path('drive/', include((images_patterns, 'images')))
]
