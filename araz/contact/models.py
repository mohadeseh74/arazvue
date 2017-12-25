from django.db import models
import datetime

class Contact(models.Model):
    name = models.CharField(blank=False, max_length=100)
    phone_number = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    email = models.EmailField(blank=False)
    checked = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name
