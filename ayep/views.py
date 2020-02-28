from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import JoinForm
from events.models import Event
from django.conf import settings
import random
import math


def index(request):
    home = 'active'
    navigation = True
    join = True
    donate = True
    recent_events = Event.objects.all()[:3]
    context = {
                'home': home,
                'join': join,
                'donate': donate,
                'navigation': navigation,
                'recent_events': recent_events,
               }
    return render(request, 'ayep/index.html', context)


def about(request):
    aboutpage = 'active'
    navigation = True
    join = True
    context = {'aboutpage': aboutpage,
               'join': join,
               'navigation': navigation,
               }
    return render(request, 'ayep/about.html', context)


def video(request):
    aboutpage = 'active'
    context = {'aboutpage': aboutpage}
    return render(request, 'ayep/video.html', context)


def detail(request, name):
    home = 'active'
    navigation = True
    context = {'home': home,
               'name': name,
               'navigation': navigation,
               }
    return render(request, 'ayep/index.html', context)


def thanksforjoining(email):
        email = email
        sendingemail = settings.EMAIL_HOST_USER
        subject = 'Welcome to Ayep'
        message = 'Thank you for joining '
        recipients = [email]
        send_mail(subject, message, sendingemail, recipients, fail_silently=True)


def send(request):
    joinform = JoinForm(request.POST)
    if joinform.is_valid():
        joinform.save()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        sendingemail = settings.EMAIL_HOST_USER
        subject = 'Joined Ayep'
        message = first_name + ' ' + last_name +' has joined AYEP.\n \n<<<<<<< email address  :  ' + email +'  >>>>>>>'
        recipients = [settings.AYEP_EMAIL]
        send_mail(subject, message, sendingemail, recipients, fail_silently=True)
        thanksforjoining(email)

        return HttpResponseRedirect(reverse('ayep:index'))

        # if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # forms = MessageForm(request.POST)
        # check whether it's valid:
        # if forms.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        # subject = forms.cleaned_data['subject']
        # message = forms.cleaned_data['message']
        # email = forms.cleaned_data['email']

            # recipients = [settings.AYEP_EMAIL]

            # send_mail(subject, message, email, recipients, fail_silently=True)
            # return HttpResponseRedirect(reverse('ayep:index'))
    # navigation = True
    return HttpResponseRedirect(reverse('ayep:index'))


def join(request):
    # home = 'active'
    # joinform = JoinForm(request.POST)
    # joinform.save()
    # if joinform.is_valid():
    # navigation = True
    # join = True
    name = request.POST['name']
    subject = 'AYEP joining link'
    email = request.POST['email']

    number1 = random.randint(68765,8967556)
    number3 = random.randint(897,7809)
    num1 = math.floor((number1 + number3)/3)
    num2 = num1*1937893
    number2 = int(num2/0.5497)

    link = 'https://www.ayep.net/' + str(number2) + '/join_form/' + str(number1) + '/' + str(number3)
    message = 'Dear ' +name + ', \n\n You are welcome to AYEP. Please follow the link below to join AYEP \n\n' + link

    sendingemail = settings.EMAIL_HOST_USER
    recipients = [email]

    send_mail(subject, message, sendingemail, recipients, fail_silently=True)
    # context = {'home': home,
    #           'navigation': navigation,
    #           'join': join,
    #           }
    return HttpResponseRedirect(reverse('ayep:index'))


def form(request):

    home = 'active'
    # name = request.POST['name']
    # subject = 'Request to join Ayep'
    # email = request.POST['email']
    # message = ' is requesting to join AYEP. '
    context = {'home': home}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # forms = MessageForm(request.POST)
        # check whether it's valid:
        # if forms.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        # subject = forms.cleaned_data['subject']
        # message = forms.cleaned_data['message']
        # email = forms.cleaned_data['email']

        # recipients = [settings.AYEP_EMAIL]

        # send_mail(subject, message, email, recipients, fail_silently=True)
        return HttpResponseRedirect(reverse('ayep:index'))

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = MessageForm()

    return render(request, 'contact/index.html', context)


def join_form(request,number2,number1,number3):
    navigation = True
    context = {
           'navigation': navigation,
           }

    if 897<= number3 <= 7809:
        if 68765<= number1 <= 8967556:
                num1 = math.floor((number1 + number3)/3)
                num2 = num1*1937893
                numx = int(num2/0.5497)

                if number2 == numx:
                    return render(request, 'ayep/join form.html', context)


    # num2 = random.randint(num1,123456789)
    # numx = math.floor(num2/0.549)
    # if numx == int(number2):
    #     return render(request, 'ayep/join form.html', context)


    return HttpResponseRedirect(reverse('ayep:index'))


# def causes(request):
#     causespage = 'active'
#     context = {'causespage': causespage}
#     return render(request, 'ayep/causes.html', context)
#
#

#
#
# def blog(request):
#     blogpage = 'active'
#     context = {'blogpage': blogpage}
#     return render(request, 'ayep/blog.html', context)


# def blogsingle(request):
#     blogpage = 'active'
#     context = {'blogpage': blogpage}
#     return render(request, 'ayep/blog-single.html', context)