from django.db import models

# Create your models here.
class DeviceList(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    devicemac = models.CharField(max_length=20, blank=True, default='')
    deviceon = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',) 
