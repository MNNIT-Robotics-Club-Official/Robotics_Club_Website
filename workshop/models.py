from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

def get_path(instance, filename):
    extension = filename.split('.')[-1]
    uuid_name = uuid.uuid1().hex
    return f'workshop/{uuid_name}.{extension}'

Status = ((0,"Past"),(1,"Upcoming"))

class Workshop(models.Model):
    title = models.CharField(blank=False,unique=False,max_length=256)
    date = models.DateField(blank=True,null=True,unique=False)
    venue = models.CharField(blank=True,null=True,max_length=256)
    target = models.CharField(max_length=256,default="All")
    link = models.FileField(upload_to=get_path,null=True,blank=True)
    image = models.ImageField(default='default-workshop.png',upload_to=get_path)
    date_posted = models.DateField()
    status = models.IntegerField(choices=Status,default=1)



    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args,**kwargs):
        self.date_posted=timezone.now().date()
        if self.date <= self.date_posted:
            self.status = 0
        super().save(args,kwargs)