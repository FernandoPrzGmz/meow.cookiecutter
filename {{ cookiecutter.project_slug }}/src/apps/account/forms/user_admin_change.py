from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    """
    Formulario para la modificación del usuario desde el admin de Django.
    
    """
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
