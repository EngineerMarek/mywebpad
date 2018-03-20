
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^NzMlVn/', admin.site.urls),
    url(r'', include('webpad.urls')),
]
