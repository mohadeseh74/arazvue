from django.db import models
import datetime
from service.models import OurService


class Country(models.Model):
    country = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.country

class Request(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    sender_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='sender')
    recipient_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='recipient')
    method = models.ForeignKey(OurService, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.email
