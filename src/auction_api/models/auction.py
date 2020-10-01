from datetime import datetime

from django.db import models

from auction_api.models.base import BaseModel


class AuctionQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(is_completed=False, expiration_date__gt=datetime.now())

    def is_closed(self):
        return self.filter(is_completed=True, expiration_date__lt=datetime.now())


class Auction(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    seller = models.ForeignKey(
        "User", verbose_name="Продавец", on_delete=models.CASCADE
    )
    start_price = models.IntegerField(verbose_name="Начальная цена")
    price_step = models.SmallIntegerField(verbose_name="Шаг цены", default=100)
    expiration_date = models.DateTimeField(verbose_name="Дата завершения аукциона")
    is_completed = models.BooleanField(default=False, verbose_name="Завершен")

    objects = AuctionQuerySet.as_manager()

    @property
    def is_active(self):
        return (
            True
            if self.expiration_date.replace(tzinfo=None) > datetime.now()
            and not self.is_completed
            else False
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "аукцион"
        verbose_name_plural = "аукционы"
