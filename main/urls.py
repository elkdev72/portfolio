from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
]