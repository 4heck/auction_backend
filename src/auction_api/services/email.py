from auction_api.constants import (
    NEW_AUCTION_SUBJECT,
    NEW_AUCTION_TEXT,
    NEW_BID_SUBJECT,
    NEW_BID_TEXT,
)
from auction_api.models import Auction, User, Bid
from auction_api.tasks import send_email


def send_new_auction_notifications(auction_instance: Auction):
    new_auction_subject = NEW_AUCTION_SUBJECT.format(
        auction_name=auction_instance.title
    )
    new_auction_text = NEW_AUCTION_TEXT.format(
        auction_name=auction_instance.title,
        auction_seller_username=auction_instance.seller.username,
        auction_created_at=auction_instance.created_at.strftime("%d.%m.%Y, %H:%M:%S"),
    )

    return send_email(
        email_list=_get_new_auction_email_list(auction_instance),
        subject=new_auction_subject,
        body=new_auction_text,
    )


def _get_new_auction_email_list(auction_instance: Auction):
    email_list = []

    for recipient in User.objects.all().exclude(pk=auction_instance.seller.pk):
        email_list.append(recipient.email)

    return list(set(email_list))


def send_new_bid_notification(bid_instance: Bid):

    new_bid_subject = NEW_BID_SUBJECT.format(auction_name=bid_instance.auction.title)
    new_bid_text = NEW_BID_TEXT.format(auction_name=bid_instance.auction.title)

    return send_email(
        email_list=_get_new_bid_email_list(bid_instance),
        subject=new_bid_subject,
        body=new_bid_text,
    )


def _get_new_bid_email_list(bid_instance: Bid):
    email_list = []

    for bid in bid_instance.auction.bid_set.all():
        email_list.append(bid.user.email)

    return list(set(email_list))
