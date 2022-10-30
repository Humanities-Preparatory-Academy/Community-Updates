from django import forms
import datetime

class JobSubmitForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    description = forms.CharField(label='description', max_length=500)
    url = forms.CharField(label='url', max_length=500)
    photo = forms.FileInput()
    time = forms.DateField()

class JobFilterForm(forms.Form):
    # sort by date
    date = forms.BooleanField()

# You can customize form widget attributes https://docs.djangoproject.com/en/4.1/ref/forms/widgets/#django.forms.Widget