from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128)#string
    subtitle = models.CharField(max_length=256)#string
    body = models.TextField() #string
    created_on = models.DateField(auto_now_add=True)#date/datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    ) #user Model/foreign key to user model