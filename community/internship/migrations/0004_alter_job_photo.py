# Generated by Django 4.0.6 on 2022-10-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0003_job_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
