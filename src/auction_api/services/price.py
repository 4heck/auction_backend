from auction_api.models import Auction, Bid


def get_last_price(auction: Auction) -> int:
    last_auction_bids = Bid.objects.filter(auction=auction).order_by("-created_at")
    if last_auction_bids:
        min_auction_price = last_auction_bids.first().price
    else:
        min_auction_price = auction.start_price + auction.price_step

    return min_auction_price


def get_min_price(auction: Auction) -> int:
    return get_last_price(auction) + auction.price_step


def validate_bid_price(price: int, auction: Auction) -> bool:
    if price < get_min_price(auction):
        return False
    else:
        return True


def validate_bid_user(auction: Auction, customer):
    if auction.seller == customer:
        return False
    else:
        return True
