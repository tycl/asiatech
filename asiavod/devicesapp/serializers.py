from rest_framework import serializers
from devicesapp.models import DeviceList

class DeviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceList
        fields =('id', 'created', 'devicemac', 'deviceon')
