from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ProjectListView(LoginRequiredMixin, ListView):
    model = models.Projects
    template_name = 'project/list.html'
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Projects_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    #success_url = reverse_lazy('Project_update')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Projects
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Projects_list')

    def test_func(self):
        return self.get_object().user_id == self.request.user.id


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = models.Task
    fields = ['description', 'projects']
    http_method_names = 'post'

    def test_func(self):
        project_id = self.request.POST.get('projects', '')
        return models.Projects.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = 'post'

    def test_func(self):
        return self.get_object().projects.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().projects.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.projects.id])
