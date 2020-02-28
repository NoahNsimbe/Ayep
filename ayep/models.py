from django.db import models
from django.utils import timezone

# Create your models here.


class Join(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='First Name ')
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Last Name ')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address ')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Phone Number ')
    date = models.DateTimeField(verbose_name='Date joined ', default=timezone.now)
    others = models.TextField(blank=True, null=True, verbose_name='Other Information ')

    class Meta:
        verbose_name = "Members"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.first_name + " " + self.last_name
