from django.db import models
from django.urls import reverse

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('image_detail', args=[str(self.id)])
