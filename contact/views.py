from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thank you for contacting us. \
                    We will be in touch as soon as possible')
            instance = contact_form.save()
            user_email = instance.email
            subject = render_to_string(
                'contact/email/email_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/email/email_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
            )

        else:
            messages.error(request, 'There was an error, \
                please check the form is valid')

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
