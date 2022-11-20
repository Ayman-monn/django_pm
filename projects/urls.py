from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Projects_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='Project_create')
]
