from django.forms import ModelForm
from .models import Donations


class DonateForm(ModelForm):
    class Meta:
        model = Donations
        fields = ['first_name', 'last_name', 'email', 'phone', 'item_donated', 'purpose']



