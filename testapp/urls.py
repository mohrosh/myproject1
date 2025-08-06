from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/upload/', views.upload_project, name='upload_project'),
    path('projects/download/<int:project_id>/', views.download_document, name='download_document'),
    path('contact/', views.contact, name='contact'),
]
