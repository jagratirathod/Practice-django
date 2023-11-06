from django.apps import AppConfig


class CustomizeAdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "customize_admin"
