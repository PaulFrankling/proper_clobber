from django.contrib import admin
from .models import ContactMessages


class ContactMessagesAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'email',
        'subject',
        'date_sent',
    )


admin.site.register(ContactMessages, ContactMessagesAdmin)
