from django.db import models





class OurService(models.Model):
    name = models.CharField(max_length=50, blank=False)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    ourservice = models.ForeignKey(OurService, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=200, null=True, allow_unicode=True)
    image = models.ImageField(blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title
