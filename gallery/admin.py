from django.contrib import admin

# Register your models here.
from .models import Images, Videos

admin.site.register(Images)
admin.site.register(Videos)
