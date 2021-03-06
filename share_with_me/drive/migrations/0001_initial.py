# Generated by Django 3.0.6 on 2020-06-05 09:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import drive.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('specialty', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('path', models.TextField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('course', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)])),
                ('specialty', models.CharField(max_length=30)),
                ('subject', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='static/default_img.png', upload_to=drive.models.content_file_name)),
                ('file', models.FileField(blank=True, null=True, upload_to=drive.models.content_file_name)),
                ('course_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drive.Image')),
            ],
        ),
    ]
