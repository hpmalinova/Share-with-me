from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Courses(models.Model):
    course = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    specialty = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    path = models.TextField(primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        self.path = f'{self.course}/{self.specialty}/{self.subject}'
        super().save(*args, **kwargs)


def content_file_name(instance, filename):
    return '{0}/{1}/{2}/{3}'.format(instance.course_path.course,
                                    instance.course_path.specialty,
                                    instance.course_path.subject,
                                    filename)


class Image(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    course_path = models.ForeignKey(Courses, to_field='path', on_delete=models.CASCADE)
    image = models.ImageField(default='static/default_img.png', upload_to=content_file_name)
    file = models.FileField(upload_to=content_file_name, blank=True, null=True)

    def clean(self):
        super().clean()
        if not self.file and self.image == 'static/default_img.png':
            raise ValidationError('You should upload a file.')

    def image_tag(self):
        if self.file:
            return mark_safe(f'<img src="{self.image.url}" title="{self.file.url}" width="250" height="150" />')
        else:
            return mark_safe(f'<img src="{self.image.url}" title="{self.image.url}" width="250" height="150" />')

    def path_to_file(self):
        return str(self.course_path)

    image_tag.short_description = 'ImageTag'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.image)


class Comments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    comment = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    file = models.ForeignKey(Image, on_delete=models.CASCADE)


class Requests(models.Model):
    username = models.CharField(max_length=50)
    course = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    specialty = models.CharField(max_length=30)
    subject = models.CharField(max_length=30, blank=True, null=True)
