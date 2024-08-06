from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    users=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

