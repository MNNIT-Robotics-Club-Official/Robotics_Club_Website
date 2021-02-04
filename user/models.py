from django.db import models
from django.contrib.auth.models import User
# Create your models here.
Branch=((0,"IT"))
Rank=((0,"Temporary Ban"),(1,"Member"),(2,"Coordinator"),(3,"Head"))
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    regnum=models.IntegerField(default=0)
    # branch=models.IntegerField(choices=Branch,default=0)
    role=models.IntegerField(choices=Rank,default=1)

    def __str__(self):
        return f'{self.user.first_name}-{self.regnum}'

