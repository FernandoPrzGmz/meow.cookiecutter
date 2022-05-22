"""
Settings for project
"""
from .django import *
from .third_party import *
from .local import *


# Se aplican las siguientes acciones si el modo debug esta desactivado
if not DEBUG:
    # Remover el middleware del django-debug-toolbar
    MIDDLEWARE.remove('debug_toolbar.middleware.DebugToolbarMiddleware')
