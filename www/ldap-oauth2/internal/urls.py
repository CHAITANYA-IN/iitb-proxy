# from django.conf.urls import include, url
# -from django.conf.urls import include, url
from django.conf.urls import include
from django.urls import re_path as url
from rest_framework.routers import DefaultRouter

from .views import InternalViewset

router = DefaultRouter()
router.register('', InternalViewset, basename='internal')

urlpatterns = [
    url('^api/', include((router.urls, 'api'), namespace='api')),
]
