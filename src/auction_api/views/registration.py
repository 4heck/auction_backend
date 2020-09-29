from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auction_api.serializers.registration import RegistrationSerializer


class RegistrationAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"token": serializer.data.get("token", None)},
            status=status.HTTP_201_CREATED,
        )
