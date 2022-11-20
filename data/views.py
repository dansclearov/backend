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

class DashboardBinViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        data = [
            {
                "date": "2020",
                "deltaUp": True,
                "newVisits": 10,
                "binsCollected": 11880,
                "totalGarbage": 712800
            },
            {
                "date": "2021",
                "deltaUp": True,
                "newVisits": 15,
                "binsCollected": 10098,
                "totalGarbage": 807840
            }
        ]
        return Response(data)
    
class DashboardBinGeneralStatsViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        data = [
            {
                "title": "Total Spend Exept IoT",
                "value": 57290,
                "activeProgress": 70,
                "description": "Better than last week (8%)"
            },
            {
                "title": "Total Spend With IoT Implementation",
                "value": 37809,
                "activeProgress": 30,
                "description": "Better than last week (15%)"
            },
            {
                "title": "Invoices",
                "value": 50,
                "activeProgress": 10,
                "description": "Better than last week (10%)"
            }
        ]
        return Response(data)

class DashboardDieselViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        data = {
            "summary": [
                {
                    "title": "Diesel 2021 (L)",
                    "value": 50510,
                },
                {
                    "title": "Diesel 2022 (L)",
                    "value": 41551,
                },
                {
                    "title": "Fuel Economy (L)",
                    "value": 8959,
                },
                {
                    "title": "Less CO2",
                    "value": 24190,
                }
            ],
            "chart": {
                "labels": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
                "data": [
                    [4234, 3420, 3600, 4820, 3550, 4306, 4190, 5600, 4950, 4620, 3119, 4101],
                    [3598, 2736, 3060, 3856, 2840, 3660, 3562, 4200, 4059, 3926, 2651, 3403]
                ]
            }
        }
        return Response(data)


class DashboardCo2ViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        data = [9714, 7396, 8262, 10411, 7516, 9072, 9617, 10340]
        return Response(data)


class DashboardBinsViewSet(viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def list(self, request):
        import json
        f = open('bins.json')
        data = json.load(f)
        return Response(data)
