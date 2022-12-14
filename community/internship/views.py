import json
import os
from dotenv import load_dotenv
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.views.decorators.clickjacking import xframe_options_exempt

import io
import base64
from PIL import Image
from django.core.files import File

from .utils.objectstorage import (
    s3_client
)

from .forms import (
    JobSubmitForm
)

from .models import Job

class Internship(View):

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):

        all_jobs = Job.objects.all()

        jobs = all_jobs.order_by('-time_posted')

        ctx = {
            "jobs": jobs
        }

        return render(request, 'internship/internships.html', ctx)

class InternshipSelective(View):

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):

        job = Job.objects.get(pk=kwargs['internship'])

        ctx = {
            "job": job
        }

        return render(request, 'internship/internship-selective.html', ctx)

class InternshipFilter(View):

    def post(self, request, *args, **kwargs):

        ctx = {
            "jobs": None
        }

        # Return in a filtered context

        return render(request, 'internship/internships.html', ctx)

class InternshipForm(View):

    def get(self, request, *args, **kwargs):

        ctx = {
            "uri": "form/"
        }

        return render(request, 'internship/form.html', ctx)

    def post(self, request, *args, **kwargs):

        form = JobSubmitForm(request.POST)

        if form.is_valid():
            
            fields = {
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "url": form.cleaned_data['url'],
                "time": form.cleaned_data['time']
            }

            Image.open(request.FILES['photo']).save(f"community/media/{request.FILES['photo'].name}")

            p = os.path.join(os.path.dirname(__file__), f"../community/media/{request.FILES['photo'].name}")
            
            # Upload Files to block storage

            client = s3_client()

            client.upload_file(p, 'humanitiesprep', request.FILES['photo'].name, ExtraArgs={'ContentType': "image/png", 'ACL':'public-read'})

            job = Job(
                    title= fields['title'],
                    description = fields['description'],
                    url = fields['url'],
                    image = f"https://humanitiesprep.nyc3.digitaloceanspaces.com/{request.FILES['photo'].name}",
                    time_posted = fields['time']
                )

            job.save()
        
            return redirect('/internships')
            
class InternshipFormUpdate(View):

    def get(self, request, *args, **kwargs):

        job = Job.objects.get(pk=kwargs['internship'])

        ctx = {
            "uri": "edit/",
            "id": job.pk,
            "title": job.title,
            "description": job.description,
            "url": job.url,
            "date": job.time_posted
        }

        return render(request, 'internship/form.html', ctx)

    def post(self, request, *args, **kwargs):

        job = Job.objects.get(pk=kwargs['internship'])

        form = JobSubmitForm(request.POST)

        if form.is_valid():

            fields = {
                    "title": form.cleaned_data['title'],
                    "description": form.cleaned_data['description'],
                    "url": form.cleaned_data['url'],
                    "time": form.cleaned_data['time']
                }

            Image.open(request.FILES['photo']).save(f"community/media/{request.FILES['photo'].name}")

            p = os.path.join(os.path.dirname(__file__), f"../community/media/{request.FILES['photo'].name}")

            client = s3_client()

            client.upload_file(p, 'humanitiesprep', request.FILES['photo'].name, ExtraArgs={'ContentType': "image/png", 'ACL':'public-read'})

            job.title = fields['title']
            job.description = fields['description']
            job.url = fields['url']
            job.image = f"https://humanitiesprep.nyc3.digitaloceanspaces.com/{request.FILES['photo'].name}"
            job.time_posted = fields['time']

            job.save()

            return redirect('/internships')