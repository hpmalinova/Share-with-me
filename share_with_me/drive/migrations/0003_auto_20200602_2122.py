# Generated by Django 3.0.6 on 2020-06-02 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0002_auto_20200602_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='path',
            field=models.TextField(blank=True, primary_key=True, serialize=False),
        ),
    ]