from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class News(models.Model):
    title = models.CharField(blank=False,unique=False,max_length=256)
    content =models.TextField()
    link = models.URLField(blank=True,null=True)
    date = models.DateField(blank=True,unique=False)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args,**kwargs):
        self.date=timezone.now()
        super().save(args,kwargs)
