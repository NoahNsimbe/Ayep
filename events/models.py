from django.db import models

# Create your models here.


class Event(models.Model):
    topic = models.CharField(max_length=255, verbose_name='Event title ')
    venue = models.CharField(max_length=255, verbose_name='Venue ')
    date = models.DateTimeField(verbose_name='Event date ')
    description = models.TextField(verbose_name='Event Description ')
    image = models.ImageField(upload_to='events/images/', verbose_name='Event image ')

    class Meta:
        verbose_name = "Events"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.topic











