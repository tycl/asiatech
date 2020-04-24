from django.contrib import admin

from .models import DeviceList, ScreenPicture

# Register your models here.

class DeviceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'devicemac', 'deviceon',)

admin.site.register(DeviceList, DeviceListAdmin)
admin.site.register(ScreenPicture)
