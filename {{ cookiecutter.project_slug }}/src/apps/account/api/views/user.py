from django.contrib.auth import get_user_model
from rest_framework import generics

from src.apps.account.api.serializers.user import UserSerializer

User = get_user_model()


class UserList(generics.ListAPIView):
    """
    View de Django REST Framework que expone los recursos
    del modelo `src.apps.account.models.User`.

    Los endpoints / recursos proporcionados en esta view consisten en:
        - [GET] - `/users/`
            - Recurso para consultar la lista de usuarios
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
