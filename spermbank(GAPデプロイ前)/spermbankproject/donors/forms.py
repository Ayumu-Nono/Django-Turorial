from django import forms
from .models import Donor,DonorSearch
from .models import HAIR
from .models import HEIGHT

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('number','hair_color','height','weight','ICI_IUI','blood_type','today_photo','profile','eye_color','mot','memo')


class DonorSreachForm(forms.ModelForm):
    class Meta:
        model = Donor
        # fields = ('number','hair_color','height','weight','ICI_IUI','blood_type','today_photo','profile','eye_color','mot')
        fields =('hair_color',)
