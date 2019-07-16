from django import forms
from .models import Donor
from .models import HAIR

class DonorForms(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('number','hair_color','height','weight','ICI_IUI','blood_type','today_photo','profile','eye_color','mot','memo')


# まずは髪色を検索できることから
HAIR = HAIR + (('','-------')) #空欄もありにするので。

class DonorSreachForm(forms.Form):
    hair_color = forms.ChoiceField(label='髪の色', choices=HAIR, required=False)


