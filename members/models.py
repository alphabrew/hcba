from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length= 50)
    join_date = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.name
