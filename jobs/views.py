from django.shortcuts import render
from .models import Project, Skills, Skilltype

# Create your views here.

def home(request):
    programming = Skills.objects.all().filter(type__name="Programming Language")
    web = Skills.objects.all().filter(type__name="Web Development")
    storage = Skills.objects.all().filter(type__name="Storage Technologies")
    software = Skills.objects.all().filter(type__name="Software")
    others = Skills.objects.all().filter(type__name="Other")
    projects = Project.objects.all()
    
    my_dict = {
        'programming' : programming,
        'web': web,
        'storage': storage,
        'software': software,
        'others': others,
        'projects': projects,
    }
    return render(request, 'jobs/home.html', my_dict)
