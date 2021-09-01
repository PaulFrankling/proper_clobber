from django import forms
from .models import ContactMessages


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessages
        fields = (
            'first_name',
            'last_name',
            'email',
            'subject',
            'message',
        )
