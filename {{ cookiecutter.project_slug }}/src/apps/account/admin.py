"""
Interfaces administración de la aplicación `src.apps.account`

"""
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from src.apps.account.forms.user_admin_change import UserAdminChangeForm
from src.apps.account.forms.user_admin_creation import UserAdminCreationForm

User = get_user_model()


# Register your models here.
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    """
    Interfaz de administración para el modelo `src.apps.account.models.User`

    """
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {
            'fields': ('username', 'password'),
        }),
        (_('Personal info'), {
            'fields': ('name', 'email'),
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        },),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
        }),
    )
    list_display = ('username', 'name', 'is_superuser')
    search_fields = ('username', 'name')
    readonly_fields = ('last_login', 'date_joined')
