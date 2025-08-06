from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from .models import Project, Contact
from .forms import ContactForm, ProjectForm
import os

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})

def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})

def download_document(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    file_path = project.document.path  # actual file path
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    return redirect('projects')
