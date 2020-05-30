import os
from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

# the settings for MEDIA_ROOT and MEDIA_URL come from the project settings
# but could be overridden in the model
# MEDIA_ROOT = '/home/<user>/project/imgproject/media_cdn'
# MEDIA_URL = '/media'

MEDIA_ROOT = 'media'


# Create your models here.
class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True)

    def url(self):
        return os.path.join(settings.MEDIA_URL, os.path.basename(str(self.image)))

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


    def __str__(self):
        return 'Image idk'
