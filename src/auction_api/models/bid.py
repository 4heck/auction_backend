from django.db import models

from auction_api.models.base import BaseModel


class Bid(BaseModel):
    auction = models.ForeignKey("Auction", verbose_name="Аукцион", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "User", verbose_name="Пользователь", on_delete=models.CASCADE
    )
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "ставка"
        verbose_name_plural = "ставки"
