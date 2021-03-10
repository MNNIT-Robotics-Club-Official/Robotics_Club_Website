from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from PIL import Image
import uuid
from django.utils import timezone


# Create your models here.
def get_path(instance, filename):
    extension = filename.split('.')[-1]
    uuid_name = uuid.uuid1().hex
    return f'blogs/{uuid_name}.{extension}'

class Blog(models.Model):
    title=models.CharField(blank=False,unique=False,max_length=50) #size changed from 256
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateField()
    vidlink=models.URLField(blank=True,unique=False)
    tags=TaggableManager(blank=True)              #changed
    image = models.ImageField(default='default-blog.png', upload_to=get_path)
    approved=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}-{self.author}'

    def save(self, *args,**kwargs):
        self.date=timezone.now()
        if not self.vidlink.find("v=")==-1:
            self.vidlink="https://www.youtube.com/embed/"+self.vidlink.split("v=",1)[1]
        super().save(args,kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail',kwargs={'pk':self.pk})

    def approve(self):
        self.approved=True
        self.save()

    def imagelink(self):
        return f'blogs/{self.pk}__{self.title}'

