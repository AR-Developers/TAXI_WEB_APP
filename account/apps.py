from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self): #method just to import the signals
    	from .import signals
