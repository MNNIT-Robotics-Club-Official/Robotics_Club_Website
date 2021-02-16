from django import forms
from .models import Component,Request

class ComponenentForm(forms.ModelForm):
    class Meta:
        model=Component
        fields=['name','max_num','type','detail']

class UpdateComponentForm(forms.ModelForm):
    class Meta:
        model=Component
        fields=['name','max_num','type','detail','issued_members']

class RequestForm(forms.ModelForm):
    class Meta:
        model=Request
        fields=['request_num','reason']

        widgets = {
            'request_num': forms.TextInput(attrs={
                'id': 'request_number',
                'required': True,
                'placeholder': 'Enter no of components'
            }),
        }