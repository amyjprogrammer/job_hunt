from django import forms

from .models import JobHunt

class JobHuntForm(forms.ModelForm):
    class Meta:
        model = JobHunt
        fields = '__all__'
