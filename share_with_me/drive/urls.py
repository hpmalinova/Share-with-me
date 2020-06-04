from django.urls import path, include

from drive.views import index, images

app_name = 'drive'

images_patterns = [
    path('courses/', images.courses, name='courses'),
    path('courses/<int:course>/', images.speciality, name='speciality'),
    path('courses/<int:course>/<str:specialty>/', images.subject, name='subject'),
    path('courses/<int:course>/<str:specialty>/<str:subject>/',
         images.detail_subject, name='detail_subject'),
    path('courses/<path:path>/upload', images.upload_file, name='upload_file'),
    path('courses/<path:path>/list/', images.list, name='list'),
    path('courses/<path:path>/<int:image_id>/', images.detail, name='detail'),
    path('courses/<path:path>/<int:image_id>/add-comment', images.add_comment, name='add_comment'),
    path('search/', images.search, name='search')
]

home_patterns = [
    path('', images.base, name='base'),
]

about_patterns = [
    path('', images.about, name='about')
]

urlpatterns = [
    path('', index, name='index'),
    path('', include((images_patterns, 'images'))),
    path('home/', include((home_patterns, 'home'))),
    path('about-us/', include((about_patterns, 'info')))
]
