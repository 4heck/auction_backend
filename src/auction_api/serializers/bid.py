from rest_framework import serializers

from auction_api.models import Bid
from auction_api.services.price import validate_bid_price, validate_bid_user


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"

    def validate(self, attrs):
        if not validate_bid_price(
            price=attrs.get("price"), auction=attrs.get("auction")
        ):
            raise serializers.ValidationError("Цена ставки невалидна")
        if not validate_bid_user(
            auction=attrs.get("auction"), customer=attrs.get("user")
        ):
            raise serializers.ValidationError(
                "Данный пользователь не может делать ставку"
            )
        return attrs

    def create(self, validated_data):
        return Bid.objects.create(**validated_data)
