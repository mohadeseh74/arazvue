from django.db import models








class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False)
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
