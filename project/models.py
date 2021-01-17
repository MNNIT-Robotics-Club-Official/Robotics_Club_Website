from django.db import models

# Create your models here.
Status=((0,"Ongoing"),(1,"Completed"),(2,"Abandoned"))
class Project(models.Model):
    title=models.CharField(blank=False,unique=False,max_length=100)
    github=models.URLField(blank=True)
    vidlink=models.URLField(blank=True)
    detail=models.TextField(blank=False)
    status=models.IntegerField(choices=Status,default=0)