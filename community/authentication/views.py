import json
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from authlib.integrations.django_client import OAuth

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

def login(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))
    return oauth.google.authorize_redirect(request, redirect_uri)

def auth(request):
    token = oauth.google.authorize_access_token(request)
    request.session['user'] = token['userinfo']
    return redirect('/internships')

def logout(request):
    request.session.pop('user', None)
    return redirect('/internships')