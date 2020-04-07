from django.shortcuts import render
from .models import Project, Skills, Skilltype

# Create your views here.

def home(request):
    programming = Skills.objects.all().filter(type__name="Programming Language").order_by('-id')
    web = Skills.objects.all().filter(type__name="Web Development").order_by('-id')
    storage = Skills.objects.all().filter(type__name="Storage Technologies").order_by(('-id'))
    software = Skills.objects.all().filter(type__name="Software").order_by(('-id'))
    others = Skills.objects.all().filter(type__name="Other").order_by(('-id'))
    projects = Project.objects.all().order_by(('-id'))
    
    my_dict = {
        'programming' : programming,
        'web': web,
        'storage': storage,
        'software': software,
        'others': others,
        'projects': projects,
    }
    return render(request, 'jobs/home.html', my_dict)
