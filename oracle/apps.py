from django.apps import AppConfig


class OracleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oracle'

    def ready(self):    # noqa: PLR6301
        from . import signals   # noqa: PLC0415,F401,I001
