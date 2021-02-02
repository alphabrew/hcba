from django.db import models
from datetime import datetime


# Create your models here.
class Announcement(models.Model):
    announcement= models.TextField(blank = True)
    is_published= models.BooleanField(default= True)
    date= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.announcement
