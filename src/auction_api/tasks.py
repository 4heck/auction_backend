from typing import Union

from django.conf import settings
from django.core.mail import send_mail as django_send_mail

from auction.celery import app


@app.task(queue="email")
def send_email(email_list: Union[list, str], subject, body):
    if isinstance(email_list, str):
        email_list = [email_list]

    emails_sent = django_send_mail(
        subject=subject,
        from_email=settings.EMAIL_FROM_EMAIL,
        recipient_list=email_list,
        message=body,
    )
    return f"{emails_sent} emails sent"
