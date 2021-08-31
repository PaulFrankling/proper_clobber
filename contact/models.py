from django.db import models


class ContactMessages(models.Model):

    class Meta:
        verbose_name = 'Received Messages'

    first_name = models.CharField(max_length=54, null=False, blank=False)
    last_name = models.CharField(max_length=54, null=False, blank=False)
    email = models.EmailField(max_length=54, null=False, blank=False)
    subject = models.CharField(max_length=54, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
