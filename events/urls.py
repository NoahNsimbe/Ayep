from django.urls import path, include

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.index, name='index'),
]