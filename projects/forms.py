from django import forms
from . import models
from django.utils.translation import gettext as _
attrs = {'class': 'form-control'}


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category', 'title', 'description']
        labels ={
            'category': _('category'),
            'title': _('title'),
            'description':_('description')
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }
