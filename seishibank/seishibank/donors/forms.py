from django import forms
from .models import Donor

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('memo',)