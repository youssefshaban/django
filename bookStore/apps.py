from django.apps import AppConfig


class BookstoreConfig(AppConfig):
    name = 'bookStore'
    def ready(self):
        from . import signals