from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title=models.CharField(blank=False,unique=False,max_length=256)
    author=models.CharField(blank=False,unique=False,max_length=256)
    content=models.TextField()
    date=models.DateField()
    vidlink=models.URLField(blank=True,unique=False)

    def __str__(self):
        return f'{self.title}-{self.author}'

    def save(self, *args,**kwargs):
        self.date=timezone.now()
        if not self.vidlink.find("v=")==-1:
            self.vidlink="https://www.youtube.com/embed/"+self.vidlink.split("v=",1)[1]
        super().save(args,kwargs)
