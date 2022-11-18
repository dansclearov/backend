from rest_framework import serializers

from data.models import Bin


class BinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bin
        fields = ['lat', 'lng', 'percentage']


class BinsCreateSerializer(serializers.Serializer):
    bins = BinSerializer(many=True)
