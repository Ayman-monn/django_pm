from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms


class ProjectListView(ListView):
    model = models.Projects
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Projects_list')


class ProjectUpdateView(UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    #success_url = reverse_lazy('Project_update')

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = models.Projects
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Projects_list')


class TaskCreateView(CreateView):
    model = models.Task
    fields = ['description', 'projects']
    http_method_names = 'post'

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = 'post'

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])
