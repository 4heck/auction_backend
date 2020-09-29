from django.contrib import admin

from auction_api.admin.auction import AuctionModelAdmin
from auction_api.admin.bid import BidModelAdmin
from auction_api.models import Bid
from auction_api.models import Auction

admin.site.register(Auction, AuctionModelAdmin)
admin.site.register(Bid, BidModelAdmin)
