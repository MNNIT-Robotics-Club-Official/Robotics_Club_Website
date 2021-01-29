from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver

class Component(models.Model):
    name=models.CharField(max_length=128,unique=False,blank=False)
    detail=models.TextField()
    max_num=models.IntegerField(default=0)
    issued_num=models.IntegerField(default=0)
    issued_members=models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(args,kwargs)

    def available(self):
        return self.max_num-self.issued_num

Status=((0,"Pending"),(1,"Accepted"),(2,"Rejected"))

class Request(models.Model):
    request_user=models.ForeignKey(User,on_delete=models.CASCADE)
    component=models.ForeignKey(Component,on_delete=models.CASCADE)
    status=models.IntegerField(choices=Status,default=0)
    request_num=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.component.name}-{self.request_user.username}'




# @receiver(m2m_changed, sender=Component, dispatch_uid="issued_num_count")
# def update_issued(sender, instance, **kwargs):
#     print(sender.issued_members.count())
#     # component=instance
#     # component.issued_num = component.issued_members.count()
#     # component.save()
#
# m2m_changed.connect(update_issued, sender=Component)