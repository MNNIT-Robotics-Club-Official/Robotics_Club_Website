from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
import uuid

# Create your models here.
def get_path(instance, filename):
    extension = filename.split('.')[-1]
    uuid_name = uuid.uuid1().hex
    return f'projects/{uuid_name}.{extension}'

Status=((0,"Ongoing"),(1,"Completed"),(2,"Abandoned"))

class Project(models.Model):
    title=models.CharField(blank=False,unique=False,max_length=100)
    aim=models.TextField(max_length=200)
    github=models.URLField(blank=True)
    vidlink=models.URLField(blank=True)
    detail=models.TextField(blank=False)
    status=models.IntegerField(choices=Status,default=0)
    comp_and_tech = models.TextField(max_length=250,blank=False,default=None)
    members=models.ManyToManyField(User)
    image=models.ImageField(default='default-project.png',upload_to=get_path)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        if not self.vidlink.find("v=")==-1:
            self.vidlink="https://www.youtube.com/embed/"+self.vidlink.split("v=",1)[1]
        super().save(args,kwargs)

