from rest_framework import serializers

from auction_api.serializers.response import LoginResponseSerializer
from auction_api.services.auth import RegistrationService


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_null=True, allow_blank=True)
    password = serializers.CharField(help_text="Пароль", required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField(allow_null=True, allow_blank=True)

    def update(self, instance, validated_data):
        raise NotImplementedError

    def create(self, validated_data):
        user = RegistrationService().register(**validated_data)
        return LoginResponseSerializer(instance=user, context=self.context).data
