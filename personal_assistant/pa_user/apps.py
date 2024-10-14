from django.apps import AppConfig


class PaUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_user'

    def ready(self) -> None:
        import pa_user.signals  # noqa
