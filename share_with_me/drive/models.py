from django.db import models
from django.utils.safestring import mark_safe


class Courses(models.Model):
    course = models.IntegerField()
    specialty = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    my_path = models.TextField(primary_key=True)

    def save(self, *args, **kwargs):
        self.my_path = f'{self.course}/{self.specialty}/{self.subject}'
        super().save(*args, **kwargs)


def content_file_name(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.course_path.course,
                                    instance.course_path.specialty,
                                    instance.course_path.subject,
                                    filename)


class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    course_path = models.ForeignKey(Courses, to_field='my_path', on_delete=models.CASCADE)
    image = models.ImageField(default='static/default_img.jpg', upload_to=content_file_name)
    file = models.FileField(upload_to=content_file_name, blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="{}" width="250" height="150" />'.format(self.image.url))

    image_tag.short_description = 'ImageTag'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.image)
