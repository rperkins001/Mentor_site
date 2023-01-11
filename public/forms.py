
from .models import *
from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField(label='Select a file')

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    resume = forms.FileField(label='Select a file')
    cover_letter = forms.CharField(widget=forms.Textarea)
    
