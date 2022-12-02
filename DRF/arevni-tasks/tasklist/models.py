from django.db import models

# Create your models here.
class Task(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    #created_at = models.DateField(auto_now_add=True)
    #updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.subject