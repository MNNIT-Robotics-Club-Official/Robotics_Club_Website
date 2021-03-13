from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
import uuid

COMPONENT_TYPE = ((0,"Development Boards"),(1,"Sensors and Electronic Components"),(2,"Motors and Motor Drivers"),(3,"Tools"),(4,"Power and Battery"),(5,"Transmitter and Receiver"),(6,"Miscellaneous"))

def get_path(instance, filename):
    extension = filename.split('.')[-1]
    uuid_name = uuid.uuid1().hex
    return f'components/{uuid_name}.{extension}'

class Component(models.Model):
    name = models.CharField(max_length=128,unique=False,blank=False)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_path,blank=True)
    type = models.IntegerField(choices=COMPONENT_TYPE,default=6)
    max_num = models.IntegerField(default=0)
    issued_num = models.IntegerField(default=0)
    issued_members = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super().save(args,kwargs)

    def available(self):
        return self.max_num-self.issued_num

    # def imagelink(self):
    #     return f'components/{self.pk}__{self.name}'

Status=((0,"Pending"),(1,"Accepted"),(2,"Rejected"))

class Request(models.Model):
    request_user = models.ForeignKey(User,on_delete=models.CASCADE)
    component = models.ForeignKey(Component,on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status,default=0)
    request_num = models.IntegerField(default=0)
    user_confirmation = models.BooleanField(default=False)
    time_confirmation = models.TimeField(auto_created=False,null=True,blank=True)
    reason = models.TextField(max_length=128,default="",null=True,blank=True)

    def __str__(self):
        return f'{self.component.name}-{self.request_user.username}'

    def accepted_by_user(self):
        self.user_confirmation=True
        self.time_confirmation=timezone.now()
        self.save()

# @receiver(m2m_changed, sender=Component, dispatch_uid="issued_num_count")
# def update_issued(sender, instance, **kwargs):
#     print(sender.issued_members.count())
#     # component=instance
#     # component.issued_num = component.issued_members.count()
#     # component.save()
#
# m2m_changed.connect(update_issued, sender=Component)