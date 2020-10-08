from auction_api.models import Bid, User


def get_customers_email_qs(bid: Bid) -> list:
    customers_pk_list = []

    for auction_bid in Bid.objects.filter(auction=bid.auction):
        customers_pk_list.append(auction_bid.user.pk)

    return User.objects.filter(id__in=list(set(customers_pk_list)))
