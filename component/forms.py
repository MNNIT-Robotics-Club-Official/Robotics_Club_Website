from django import forms
from .models import Component

class ComponenentForm(forms.ModelForm):
    class Meta:
        model=Component
        fields=['name','max_num','detail']

class UpdateComponentForm(forms.ModelForm):
    class Meta:
        model=Component
        fields=['name','max_num','detail','issued_members']