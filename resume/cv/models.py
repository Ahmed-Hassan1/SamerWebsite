from django.db import models

# Create your models here.

class HomeVideo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    video = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name
    

class WorkVideo(models.Model):
    name = models.CharField(max_length=200)
    vide_title=models.CharField(max_length=200)
    job_title=models.CharField(max_length=200)
    video = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name