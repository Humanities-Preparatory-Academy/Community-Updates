from django.db import models

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    time_posted = models.DateTimeField()
