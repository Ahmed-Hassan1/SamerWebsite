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

class AboutMeHeader(models.Model):
    header=models.CharField(max_length=200)

    def __str__(self):
        return self.header

class AboutMeParagrapgh(models.Model):
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.description
    

class SocialMedia(models.Model):
    facebook=models.CharField(max_length=250,null=True,blank=True)
    instagram=models.CharField(max_length=250,null=True,blank=True)
    youtube=models.CharField(max_length=250,null=True,blank=True)
    twitter=models.CharField(max_length=250,null=True,blank=True)


class Contact(models.Model):
    address=models.CharField(max_length=250,null=True,blank=True)
    phone=models.CharField(max_length=250,null=True,blank=True)