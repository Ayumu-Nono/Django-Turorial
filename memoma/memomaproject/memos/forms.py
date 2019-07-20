from django import forms
from .models import Memos

class MemosForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('create_time','title','sammary','slogan','fact','abstraction','diverse')
