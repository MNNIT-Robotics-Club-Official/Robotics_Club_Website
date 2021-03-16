from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
Branch = ((0, "Biotechnology"), (1, "Civil Engineering"), (2, "Electrical Engineering"), (3, "Mechanical Engineering"), (4, "Computer Science and Engineering"),
          (5, "Electronics and Communication Engineering"), (6, "Production and Industrial Engineering"), (8, "Information Technology"), (9, "Chemical Engineering"),)

Rank = ((0, "Temporary Ban"), (1, "Member"), (2, "Coordinator"), (3, "Head"))

User._meta.get_field('email')._unique = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=False, max_length=256, unique=False)
    last_name = models.CharField(blank=True, max_length=256, unique=False)
    regnum = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField(choices=Branch, blank=True, null=True)
    role = models.IntegerField(choices=Rank, default=1)
    linkedin = models.URLField(blank=True,null=True)
    phone = models.BigIntegerField(blank=True,null=True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])

    def __str__(self):
        return f'{self.user.username}-{self.user.pk}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
