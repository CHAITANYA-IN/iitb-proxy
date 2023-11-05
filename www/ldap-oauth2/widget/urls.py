# from django.conf.urls import url
from django.urls import re_path as url
from .views import LoginWidget

urlpatterns = [
    url(r'login/$', LoginWidget.as_view(), name='login'),
]
