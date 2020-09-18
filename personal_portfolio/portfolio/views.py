"""View de la página inicial"""
from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def home(request):
    """Se llaman a los objetos dentro del modelo Project"""
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
