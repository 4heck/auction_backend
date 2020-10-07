from auction_api.constants import NEW_AUCTION_SUBJECT, NEW_AUCTION_TEXT
from auction_api.models import Auction, User
from auction_api.tasks import send_email


def send_auction_notifications(auction_instance: Auction):
    new_auction_subject = NEW_AUCTION_SUBJECT.format(
        auction_name=auction_instance.title
    )
    new_auction_text = NEW_AUCTION_TEXT.format(
        auction_name=auction_instance.title,
        auction_seller_username=auction_instance.seller.username,
        auction_created_at=auction_instance.created_at.strftime("%d.%m.%Y, %H:%M:%S"),
    )

    email_list = []
    for recipient in User.objects.all().exclude(pk=auction_instance.seller.pk):
        email_list.append(recipient.email)

    send_email(
        email_list=email_list, subject=new_auction_subject, body=new_auction_text
    )
