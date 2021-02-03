from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title=models.CharField(blank=False,unique=False,max_length=256)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateField()
    vidlink=models.URLField(blank=True,unique=False)
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