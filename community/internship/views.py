import json
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.views.decorators.clickjacking import xframe_options_exempt

from .forms import (
    JobSubmitForm
)

from .models import Job

class Internship(View):

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):

        all_jobs = Job.objects.all()

        ctx = {
            "jobs": all_jobs
        }

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

            job = Job(
                    title= fields['title'],
                    description= fields['description'],
                    url = fields['url'],
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

            job.title = fields['title']
            job.description = fields['description']
            job.url = fields['url']
            job.time_posted = fields['time']

            job.save()

            return redirect('/internships')