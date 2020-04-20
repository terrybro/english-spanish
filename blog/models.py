from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=200)
    docfile = models.FileField(null=True) 
