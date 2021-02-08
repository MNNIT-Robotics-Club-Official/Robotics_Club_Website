from django import forms
from project.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title','aim','detail','status','vidlink','github','members','image','tags']