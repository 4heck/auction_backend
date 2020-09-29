from django.contrib import admin

from auction_api.admin.auction import AuctionModelAdmin
from auction_api.models.auction import Auction

admin.site.register(Auction, AuctionModelAdmin)
