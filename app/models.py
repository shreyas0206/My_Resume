from django.db import models

# Create your models here.
class Project(models.Model):
    p_name = models.CharField(max_length=100)
    p_skills = models.CharField(max_length=400)
    p_details = models.CharField(max_length=1000)
