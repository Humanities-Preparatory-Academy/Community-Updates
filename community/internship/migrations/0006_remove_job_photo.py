# Generated by Django 4.0.6 on 2022-10-30 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0005_alter_job_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='photo',
        ),
    ]
