from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', widget=forms.Textarea)

