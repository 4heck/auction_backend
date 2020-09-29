from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def update(self, instance, validated_data):
        return super(UserSerializer, self).update(instance, validated_data)
