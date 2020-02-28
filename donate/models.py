from django.db import models
from django.utils import timezone

# Create your models here.


class Donations(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='First Name ')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name ')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address ')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Phone Number ')
    date = models.DateTimeField(verbose_name='Date of donation ', default=timezone.now)
    item_donated = models.TextField(blank=False, null=False, verbose_name='Item donated ')
    purpose = models.TextField(blank=True, null=True, verbose_name='Reason for donation ')

    class Meta:
        verbose_name = "Donations"
        verbose_name_plural = "Donations"

    def __str__(self):
        return self.first_name + " donated " + self.item_donated


