from django.db import models

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    time_posted = models.DateTimeField()
