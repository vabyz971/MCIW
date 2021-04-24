from django.apps import AppConfig


class MciwConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MCIW'

    def ready(self):
        import MCIW.signals
