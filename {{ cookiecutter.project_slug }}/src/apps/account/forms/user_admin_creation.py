from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Formulario para la creación del usuario desde el admin de Django.

    Para cambiar la forma de registrar un usuario, consulte UserSignupForm y
    UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            'username': {
                'unique': _('This username has already been taken.'),
            }
        }
