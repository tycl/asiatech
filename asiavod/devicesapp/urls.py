from django.conf.urls import url
from devicesapp import views

urlpatterns = [
    url(r'^devicesapp/$', views.device_list),
    url(r'^devicesapp/(?P<id>[0-9]+)/$', views.device_detail),
]
