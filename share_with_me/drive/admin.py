from django.contrib import admin
from drive.models import Image, Courses


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    list_display = ('image_tag', 'description', 'image', 'file', 'course_path')
    readonly_fields = ('image_tag',)


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course', 'specialty', 'subject', 'my_path')
