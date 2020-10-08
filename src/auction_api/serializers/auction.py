from rest_framework import serializers

from auction_api.models import Auction, Bid
from auction_api.serializers.bid import BidSerializer


class AuctionSerializer(serializers.ModelSerializer):
    bids = serializers.SerializerMethodField()

    class Meta:
        model = Auction
        fields = "__all__"

    def create(self, validated_data):
        return super(AuctionSerializer, self).create(validated_data)

    def get_bids(self, auction: Auction):
        bids = Bid.objects.filter(auction=auction)
        return BidSerializer(instance=bids, many=True).data
