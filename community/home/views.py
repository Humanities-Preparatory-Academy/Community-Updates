import json
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'home/home.html')