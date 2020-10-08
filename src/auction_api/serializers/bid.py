from rest_framework import serializers

from auction_api.models import Bid
from auction_api.serializers.user import UserSerializer
from auction_api.services.customers import get_customers_email_qs
from auction_api.services.price import validate_bid_price, validate_bid_user


class BidSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField()

    class Meta:
        model = Bid
        fields = (
            "customers",
            "price",
            "user",
            "auction",
        )

    def validate(self, attrs):
        if not validate_bid_price(
            price=attrs.get("price"), auction=attrs.get("auction")
        ):
            raise serializers.ValidationError({"price": "Цена ставки невалидна"})
        if not validate_bid_user(
            auction=attrs.get("auction"), customer=attrs.get("user")
        ):
            raise serializers.ValidationError(
                {"user": "Данный пользователь не может делать ставку"}
            )
        return attrs

    def create(self, validated_data):
        return Bid.objects.create(**validated_data)

    def get_customers(self, obj: Bid):
        return UserSerializer(instance=get_customers_email_qs(obj), many=True).data
