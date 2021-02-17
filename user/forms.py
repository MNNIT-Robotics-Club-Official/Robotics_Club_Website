from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email Already Exists')
       return self.cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['first_name','last_name','regnum','branch']
        exclude = ('user','role')

class PasswordResetForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password_1 = forms.CharField(widget=forms.PasswordInput)
    new_password_2 = forms.CharField(widget=forms.PasswordInput)