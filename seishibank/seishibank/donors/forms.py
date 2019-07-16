from django import forms
from .models import Donor,DonorSearch

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('blood_type','hair_color','height','memo')


    
class SearchForm(forms.ModelForm):
    class Meta:
        model  = DonorSearch
        fields = ('family_name',)