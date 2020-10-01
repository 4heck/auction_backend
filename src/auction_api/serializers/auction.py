from rest_framework import serializers

from auction_api.models import Auction


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

    def create(self, validated_data):
        return super(AuctionSerializer, self).create(validated_data)
