from django.apps import AppConfig


class TiendaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Tienda'

    def ready(self):
        import Apps.Tienda.signals  # Importa tus señales
