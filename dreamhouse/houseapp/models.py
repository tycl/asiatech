from django.db import models
import uuid

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class HouseList(models.Model):
    project = models.CharField(max_length=250, blank=True, default='')
    name = models.CharField(max_length=250, blank=True, default='')
    address = models.CharField(max_length=250, blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upload = models.FileField(upload_to=user_directory_path)
    macnum = models.UUIDField(primary_key=False, default=uuid.uuid1, editable=False)

    class Meta:
        ordering = ('name',)
