from django import forms

from .models import Donor

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('family_name','first_name','blood_type','birth_place','memo')