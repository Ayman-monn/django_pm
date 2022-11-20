from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from . import models, forms


class ProjectListView(ListView):
    model = models.Projects
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Projects_list')