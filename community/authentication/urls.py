from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('auth/', auth, name='auth'),
    path('info/', info, name='info')
]