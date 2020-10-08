from auction_api.models import Auction, Bid


def get_last_price(auction: Auction) -> int:
    last_auction_bids = Bid.objects.filter(auction=auction).order_by("-created_at")

    return (
        last_auction_bids.first().price
        if last_auction_bids
        else auction.start_price + auction.price_step
    )


def get_min_price(auction: Auction) -> int:
    return get_last_price(auction) + auction.price_step


def validate_bid_price(price: int, auction: Auction) -> bool:
    return False if price < get_min_price(auction) else True


def validate_bid_user(auction: Auction, customer):
    return False if auction.seller == customer else True
