from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from auction_api.serializers.user import UserSerializer


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.SerializerMethodField(help_text="Токен для пользователя")
    user = serializers.SerializerMethodField()

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

    @swagger_serializer_method(serializer_or_field=UserSerializer)
    def get_user(self, user):
        return UserSerializer(user, context=self.context).data

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
