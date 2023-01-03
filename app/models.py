from django.db import models

# Create your models here.

class tasks(models.Model):
    text=models.CharField(max_length=10)
    def __str__(self):
        return self.text
