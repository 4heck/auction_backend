from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from auction_api.models import Bid
from auction_api.serializers.bid import BidSerializer
from auction_api.services.email import send_new_bid_notification


class BidAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BidSerializer
    queryset = Bid.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        bid_instance = serializer.save()
        send_new_bid_notification(bid_instance=bid_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name="bid_id", in_="query", type=openapi.TYPE_INTEGER),
        ]
    )
    def get(self, request):
        return Response(
            self.serializer_class(
                instance=get_object_or_404(Bid, pk=request.query_params.get("bid_id"))
            ).data
        )
