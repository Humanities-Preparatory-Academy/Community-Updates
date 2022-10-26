from django.urls import path

from .views import (
    Internship,
    InternshipForm,
    InternshipFormUpdate
)

urlpatterns = [
    path('', Internship.as_view(), name='internship'),
    path('form/', InternshipForm.as_view(), name='internship-form'),
    path('edit/<int:internship>', InternshipFormUpdate.as_view(), name='internship-update-form')
]