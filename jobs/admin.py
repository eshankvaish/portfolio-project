from django.contrib import admin
from .models import Project, Skills, Skilltype
# Register your models here.

admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Skilltype)