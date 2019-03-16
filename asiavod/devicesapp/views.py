from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from devicesapp.models import DeviceList
from devicesapp.serializers import DeviceListSerializer


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']= 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def device_list(request):
    if request.method == 'GET':
        devicelist = DeviceList.objects.all()
        devicelist_serializer = DeviceListSerializer(devicelist, many=True)
        return JSONResponse(devicelist_serializer.data)

    elif request.method == 'POST':
        devicelist_data = JSONParser().parse(request)
        devicelist_serializer = DeviceListSerializer(data=devicelist_data)
        if devicelist_serializer.is_valid():
            devicelist_serializer.save()
            return JSONResponse(devicelist_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(devicelist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def device_detail(request, id):
    try:
        device = DeviceList.objects.get(id=id)
    except DeviceList.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        device_serializer = DeviceListSerializer(device)
        return JSONResponse(device_serializer.data)

    elif request.method == 'PUT':
        device_data = JSONParser().parse(request)
        device_serializer = DeviceListSerializer(device, data=device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JSONResponse(device_serializer.data)
        return JSONResponse(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        device.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    
