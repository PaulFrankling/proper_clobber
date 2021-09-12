""" Contact forms.py """
from django import forms
from .models import ContactMessages


class ContactForm(forms.ModelForm):
    """ Form to contact site owner """
    class Meta:
        model = ContactMessages
        fields = (
            'first_name',
            'last_name',
            'email',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
