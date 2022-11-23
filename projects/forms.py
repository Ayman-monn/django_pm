from django import forms
from . import models


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category', 'title', 'description']
        widgit = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category', 'title', 'status']
        widgit = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'status': forms.Select()
        }
