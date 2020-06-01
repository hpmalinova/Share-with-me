from django.db import models
from django.utils.safestring import mark_safe

# MEDIA_ROOT = "media"


def content_file_name(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.course, instance.speciality, instance.subject, filename)


# Create your models here.
class Image(models.Model):
    course = models.IntegerField()
    speciality = models.TextField()
    subject = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    image = models.ImageField(default='static/default_img.jpg', upload_to=content_file_name)
    file = models.FileField(upload_to=content_file_name, blank=True, null=True)

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="250" height="150" />'.format(self.image.url))
    image_tag.short_description = 'ImageTag'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.image)
