from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MessageForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request):
    navigation = True
    contactpage = 'active'
    context = {'contactpage': contactpage,
               'navigation': navigation,
               }
    return render(request, 'contact/index.html', context)


def form(request):

    contactpage = 'active'
    # name = request.POST['name']
    subject = request.POST['subject']
    email = request.POST['email']
    message = request.POST['message'] +  '\n \n \nPlease reply to   <<<<<<< sender email address  :  ' + email +'  >>>>>>>'
    context = {'contactpage': contactpage}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # forms = MessageForm(request.POST)
        # check whether it's valid:

        # subject = 'Thank you for registering to our site'
        # message = ' it  means a world to us '
        sendingemail = settings.EMAIL_HOST_USER

        recipients = [settings.AYEP_EMAIL]

        send_mail(subject, message, sendingemail, recipients, fail_silently=True)
        return HttpResponseRedirect(reverse('ayep:index'))


        # if forms.is_valid():
        #     # process the data in form.cleaned_data as required
        #     # ...
        #     # redirect to a new URL:
        #     # subject = forms.cleaned_data['subject']
        #     # message = forms.cleaned_data['message']
        #     subject = 'Thank you for registering to our site'
        #     message = ' it  means a world to us '
        #     email = settings.EMAIL_HOST_USER

        #     recipients = ['nsimbenoah@gmail.com']

        #     send_mail(subject, message, email, recipients, fail_silently=True)
        #     return HttpResponseRedirect(reverse('ayep:index'))

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = MessageForm()

    return render(request, 'contact/index.html', context)


def location(request):
    contactpage = 'active'
    context = {'contactpage': contactpage}
    return render(request, 'contact/location.html', context)
