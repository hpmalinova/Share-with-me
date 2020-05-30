from django.core.files.storage import FileSystemStorage
from django.db import models
# from django.utils.html import mark_safe


fs = FileSystemStorage(location='/media/shared_files')


class Picture(models.Model):
    name = models.CharField(max_length=250, unique=True)
    data = models.ImageField(storage=fs)

    def __str__(self):
        return self.name


'''
    def image_tag(self):
        return mark_safe('<img src="/media/shared_files/%s" width="150" height="150" />' % (self.name))

    image_tag.short_description = 'Image'
'''
