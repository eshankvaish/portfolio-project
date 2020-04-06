from django.db import models

# Create your models here.

class Skilltype(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skills(models.Model):
    type = models.ForeignKey(Skilltype, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    time = models.CharField(max_length=150)
    summary = models.TextField(max_length=500)
    url = models.URLField()

    def __str__(self):
        return self.title


    

