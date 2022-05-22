from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountConfig(AppConfig):
    """
    Clase que representa la aplicación `account` en Django y su configuración

    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.account'
    label = 'account'
    verbose_name = _('Users')
