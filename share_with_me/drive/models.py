import os
from django.db import models
from django.utils.safestring import mark_safe
from share_with_me.settings import MEDIA_ROOT, MEDIA_URL


# Create your models here.
class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True)

    def url(self):
        image_name = os.path.basename(str(self.image))
        a = os.path.join(MEDIA_URL, image_name)
        print('AAAAAAAAAAAAAAAAAAAAAAA', a)
        return a

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = 'ImageTag'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.image)
