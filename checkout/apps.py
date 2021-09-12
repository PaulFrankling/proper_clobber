""" Checkout apps.py """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout app """
    name = 'checkout'

    def ready(self):
        import checkout.signals
