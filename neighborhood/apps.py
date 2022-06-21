from django.apps import AppConfig


class NeighborhoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighborhood'

    def ready(self):
        import neighborhood.signals
