from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from auction_api.serializers.auth import RegisterSerializer
from auction_api.serializers.response import LoginResponseSerializer


class RegisterAPIView(GenericAPIView):
    """Register"""

    serializer_class = RegisterSerializer

    @swagger_auto_schema(responses={201: LoginResponseSerializer})
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data)
