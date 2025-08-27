from django.apps import AppConfig


class IceCreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream'
    # verbose_name - как будет отобрадаться на сайте приложение IceCream
    verbose_name = 'Каталог мороженого'
