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

class Home(View):

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):

        all_jobs = Job.objects.all()

        ctx = {
            "jobs": all_jobs
        }

        return render(request, 'core/base/home.html', ctx)