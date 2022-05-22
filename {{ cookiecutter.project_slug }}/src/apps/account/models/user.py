from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Modelo que representa a un Usuario de la aplicación

    """
    # Remove the first_name and last_name cols in the AbstractUser model
    first_name = None  # :type: ignore
    last_name = None  # :type: ignore

    # First and last name do not cover name patterns around the globe
    name = models.CharField(
        verbose_name=_('Name of user'),
        blank=True,
        max_length=255,
    )
