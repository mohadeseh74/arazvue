from django.db import models








class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False)

    def __str__(self):
        return self.title
