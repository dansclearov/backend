from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import BinsCreateSerializer, BinsListSerializer
from .models import Bin

class BinsViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.IsAuthenticated]

    custom_serializer_classes = {
        "create": BinsCreateSerializer,
        "list": BinsListSerializer,
    }

    def create(self, request):
        serializer = BinsCreateSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        for bin_values in serializer.validated_data['bins']:
            bin = Bin(**bin_values)
            bin.save()
        return Response(serializer.validated_data)

    def list(self, request):
        bins = Bin.objects.all()
        serializer = BinsListSerializer(bins, many=True)
        return Response({"bins": serializer.data})
