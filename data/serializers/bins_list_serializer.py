from rest_framework import serializers

from data.models import Bin


class BinsListSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    percentage = serializers.IntegerField()
