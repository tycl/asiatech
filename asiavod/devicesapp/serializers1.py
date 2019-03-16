from rest_framework import serializers
from devicesapp.models import DeviceList

class DeviceListSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    created = serializers.CharField(max_length=20)
    devicemac = serializers.CharField(max_length=20)
    deviceon = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return DeviceList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.created = validated_data.get('created', instance.created)
        instance.devicemac = validated_data.get('devicemac', instance.devicemac)
        instance.deviceon = validated_data.get('deviceon', instance.deviceon)
        instance.save()
