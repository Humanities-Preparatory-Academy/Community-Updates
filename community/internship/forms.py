from django import forms
import datetime

class JobSubmitForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    description = forms.CharField(label='description', max_length=500)
    url = forms.CharField(label='url', max_length=500)
    time = forms.DateField()