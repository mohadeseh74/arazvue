from django.db import models
import datetime
# from service.models import OurService


# class Country(models.Model):
#     country = models.CharField(max_length=20, blank=False)
#
#     def __str__(self):
#         return self.country

class Request(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    sender = models.CharField(max_length=50, blank=False, null=True)
    recipient = models.CharField(max_length=50, blank=False, null=True)
    goods_type = models.CharField(max_length=50, blank=False, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    dimentions = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField(blank=False)
    email = models.EmailField(blank=True)
    method = models.CharField(max_length=50, blank=False)
    checked = models.BooleanField(default=False)
    created_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
