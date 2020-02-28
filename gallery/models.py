from django.db import models

# Create your models here.


class Images(models.Model):
    name = models.CharField(max_length=255, verbose_name='Image name ', blank=True, null=True)
    image = models.ImageField(upload_to='gallery/images')

    class Meta:
        verbose_name = "Images"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name


class Videos(models.Model):
    name = models.CharField(max_length=255, verbose_name='Video name ', blank=True, null=True)
    video = models.URLField(max_length=300, verbose_name='Video url ')

    class Meta:
        verbose_name = "Videos"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.name
