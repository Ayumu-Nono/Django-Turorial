from django import forms
from .models import Memos

class Memos(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('create_time','title','sammary','slogan','fact','abstraction','diverse')
