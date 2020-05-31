from django.contrib import admin
from drive.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    list_display = ('image_tag', 'description', 'image', 'file')
    readonly_fields = ('image_tag',)
