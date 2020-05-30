from django.contrib import admin
from drive.models import Picture
from django.utils.html import mark_safe


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'data',)
    readonly_fields = ["data_image"]

    def data_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.data.url,
            width=obj.data.width,
            height=obj.data.height
        ))
