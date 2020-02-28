from django.urls import path

from . import views

app_name = 'donate'
urlpatterns = [
    path('', views.index, name='index'),
    path('donation/', views.donation, name='donation'),
]