# Generated by Django 4.0.6 on 2022-10-30 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0006_remove_job_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
