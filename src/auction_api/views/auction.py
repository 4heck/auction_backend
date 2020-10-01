from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auction_api.serializers.auction import AuctionSerializer


class AuctionAPIView(GenericAPIView):
    # TODO: какой-то баг тут происходит при IsAuthenticated
    permission_classes = [AllowAny]
    serializer_class = AuctionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
