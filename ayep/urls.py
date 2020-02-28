from django.urls import path

from . import views

app_name = 'ayep'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('video/', views.video, name='video'),
    # path('Blog', views.blog, name='blog'),
    # path('Causes', views.causes, name='causes'),
    # path('Blogsingle', views.blogsingle, name='blog-single'),
    path('form/', views.form, name='form'),
    # path('join_form/', views.join_form, name='join_form'),
    path('join/', views.join, name='join'),
    path('send/', views.send, name='send'),
    path('<int:name>', views.detail, name='detail'),
    path('<int:number2>/join_form/<int:number1>/<int:number3>', views.join_form, name='join_form'),
]