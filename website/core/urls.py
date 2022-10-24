from django.urls import path

from . routes.base import (
    Home,
    SiteForm
)

from . routes.auth import (
    login,
    logout,
    auth,
    info
)

urlpatterns = [
    path('home/', Home.as_view(), name='home-view'),
    path('form/', SiteForm.as_view(), name='form-view'),
    path('login/', login),
    path('logout/', logout),
    path('auth/', auth, name='auth'),
    path('info/', info, name='info')
]