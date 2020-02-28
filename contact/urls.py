from django.urls import path, include

from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('location/', views.location, name='location'),
]