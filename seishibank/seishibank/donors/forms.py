from django import forms
from .models import Donor,DonorSearch

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('number','hair_color','height','weight','ICI_IUI','blood_type','today_photo','profile','eye_color','mot','memo')


    
class SearchForm(forms.ModelForm):
    class Meta:
        model  = DonorSearch
        fields = ('family_name',)