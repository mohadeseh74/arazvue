from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False)
    link = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    address = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.address

class Phone(models.Model):
    phone = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.phone)


class Statistic(models.Model):
    name = models.CharField(max_length=100, blank=False)
    number = models.IntegerField(blank=False)

class OpeningHour(models.Model):
    day = models.CharField(max_length=100, blank=False)
    time = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.day

class SocialNetwork(models.Model):
    telegram = models.CharField(max_length=100, blank=False)
    instagram = models.CharField(max_length=100, blank=False)

class Newsletter(models.Model):
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.email
