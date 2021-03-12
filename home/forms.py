from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label='First Name')
    email = forms.EmailField(label='email')
    body = forms.CharField(min_length=10,max_length=1000,label='Message',widget=forms.Textarea(attrs={'rows':4,'col':2}))
