from django import forms
from django.forms import ModelForm
from .models import Join


class JoinForm(ModelForm):
    class Meta:
        model = Join
        fields = ['first_name', 'last_name', 'email', 'phone', 'others']





