# from django.conf.urls import url
# from django.conf.urls import url
from django.urls import re_path as url
 

from .views import LoginView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
