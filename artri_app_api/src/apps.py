from django.apps import AppConfig


class SrcConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src"
    label = "authentication"

    def ready(self):
        from src.domains.accounts import signals  # noqa: F401
