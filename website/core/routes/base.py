import json
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from django.views.decorators.clickjacking import xframe_options_exempt

from authlib.integrations.django_client import OAuth

from core.forms.job import (
    JobSubmitForm
)

from core.models.job import (
    Job
)

import datetime

class SiteForm(View):

    def get(self, request, *args, **kwargs):

        form = JobSubmitForm()

        fields = form.fields

        ctx = {
            "date": datetime.date.today(),
            "fields": fields
        }

        return render(request, 'core/base/form.html', ctx)

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

            return redirect('/app/home')

class SiteEditForm(View):

    def get(self, request, *args, **kwargs):

        id = kwargs['post_id']

        form = JobSubmitForm()

        fields = form.fields

        job = Job.objects.get(pk=id)

        ctx = {
            "date": datetime.date.today(),
            "fields": fields,
            "field_title": job.title,
            "field_description": job.description,
            "field_url": job.url,
            "field_time": job.time_posted,
            "job_id": id,
            "endpoint": "edit"
        }

        return render(request, 'core/base/form.html', ctx)

    def post (self, request, *args, **kwargs):

        form = JobSubmitForm(request.POST)

        id = kwargs['post_id']

        if form.is_valid():
            
            fields = {
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "url": form.cleaned_data['url'],
                "time": form.cleaned_data['time']
            }

            job = Job.objects.get(pk=id)

            job.title = fields['title']
            job.description = fields['description']
            job.url = fields['url']
            job.time = fields['time']

            job.save()

        return render(request, 'core/base/home.html')

class Home(View):

    # Make the page embeddable onto other web pages

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):

        all_jobs = Job.objects.all()

        ctx = {
            "jobs": all_jobs
        }

        return render(request, 'core/base/home.html', ctx)