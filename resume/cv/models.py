from django.db import models

# Create your models here.

class HomeVideo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    video = models.FileField()

    def __str__(self):
        return self.name