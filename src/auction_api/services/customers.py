from auction_api.models import Bid, User


def get_customers_email_qs(bid: Bid) -> list:
    customers_pk_list = []
    auction_bids = Bid.objects.filter(auction=bid.auction)

    for auction_bid in auction_bids:
        customers_pk_list.append(auction_bid.user.pk)

    customers_pk_list = list(set(customers_pk_list))
    customers_email_qs = User.objects.filter(id__in=customers_pk_list)

    return customers_email_qs
