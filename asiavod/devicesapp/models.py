from django.db import models
from asiatech.resources import screenname, macnumber


filename = screenname(macnumber())

# Create your models here.
class DeviceList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    devicemac = models.CharField(max_length=20, blank=True, default='')
    deviceon = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ScreenPicture(models.Model):
    device = models.ForeignKey(DeviceList, on_delete=models.CASCADE)
    fileupload = models.FileField(upload_to=filename)
    comment = models.CharField(max_length=20, blank=True, default='')

    class Meta:
        ordering = ('device',)
