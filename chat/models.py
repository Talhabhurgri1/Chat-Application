from django.db import models
from django.contrib.auth.models import User
import datetime


class chatUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    User._meta.get_field('email')._unique = True
    date_created = models.DateTimeField(default=datetime.datetime.now())
    phone_number = models.CharField(default=0, max_length=14)