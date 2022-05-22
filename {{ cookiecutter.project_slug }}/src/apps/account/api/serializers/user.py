from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer del modelo `src.apps.account.models.User`

    """
    class Meta:
        model = User
        exclude = ('password',)
