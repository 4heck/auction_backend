from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from auction.yasg import AuctionSchemaGenerator

# urlpatterns = [
#     path("direction", DirectionAPIView.as_view()),
#     path("init/", InitAPIView.as_view()),
#     path("application/", ApplicationAPIView.as_view()),
# ]

urlpatterns = []

router = SimpleRouter()

# router.register("country", CountryViewSet, basename="country")

# urlpatterns += router.urls

schema_view = get_schema_view(
    openapi.Info(title="Auction API", default_version="v1",),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
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
