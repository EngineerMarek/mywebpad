from django.conf.urls import url
from . import views

app_name= 'webpad'

urlpatterns = [
    url(r'^$', views.pad_list, name='pad_list'),
    url(r'^pad/new/$', views.new_pad, name='new_pad'),
]
