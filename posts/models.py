from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.

class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=200, help_text="Write a description about the status")
    
    def __str__(self):
        return f"{self.name}"
    

class Post(models.Model):
    title = models.CharField(max_length=128)#string
    subtitle = models.CharField(max_length=256)#string
    body = models.TextField() #string
    created_on = models.DateField(auto_now_add=True)#date/datetime
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    ) #user Model/foreign key to user model
    def __str__(self): #to string method
        return f"{self.title}"
    
    satus = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING
    )
    
    def get_absolute_url(self): #redirects the user on a Post post request
        return reverse("post_detail", args=[self.id])
    
