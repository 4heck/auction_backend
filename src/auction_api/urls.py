from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# from rest_framework.routers import SimpleRouter

from auction.yasg import AuctionSchemaGenerator
from auction_api.views.registration import RegistrationAPIView
from auction_api.views.login import LoginAPIView
from auction_api.views.auction import AuctionAPIView
from auction_api.views.bid import BidAPIView

urlpatterns = [
    re_path(
        r"^registration/?$", RegistrationAPIView.as_view(), name="user_registration"
    ),
    re_path(r"^login/?$", LoginAPIView.as_view(), name="user_login"),
    re_path(r"^auction/?$", AuctionAPIView.as_view(), name="auction"),
    re_path(r"^bid/?$", BidAPIView.as_view(), name="bid"),
]

# router = SimpleRouter()
#
# router.register("auction", AuctionViewSet, basename="auction")
#
# urlpatterns += router.urls

schema_view = get_schema_view(
    openapi.Info(title="Auction API", default_version="v1",),
    public=False,
    permission_classes=(permissions.AllowAny,),
    generator_class=AuctionSchemaGenerator,
    patterns=urlpatterns,
)

urlpatterns += [
    path(
        "swagger/<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="swagger-yaml",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger_ui/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
