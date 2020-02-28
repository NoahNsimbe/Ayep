from django.shortcuts import render
from .forms import DonateForm
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


def index(request):
    donatepage = 'active'
    navigation = True
    join = True
    context = {
                'donatepage': donatepage,
                'navigation': navigation,
                'join': join,
               }
    return render(request, 'donate/index.html', context)


def donation(request):
    donate_form = DonateForm(request.POST)
    if donate_form.is_valid():
        donate_form.save()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        item_donated = request.POST['item_donated']
        purpose = request.POST['purpose']

        subject = "Donation"
        message = first_name + ' ' + last_name + ' wishes to donate ' + item_donated + '\n Purpose : ' +  purpose + '\n Email Address : '+ email

        sendingemail = settings.EMAIL_HOST_USER
        recipients = [settings.AYEP_EMAIL]
        send_mail(subject, message, sendingemail, recipients, fail_silently=True)

    return HttpResponseRedirect(reverse('ayep:index'))


