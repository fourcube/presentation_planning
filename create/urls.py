from django.conf.urls import url

from .views import new

urlpatterns = [
    url(r'^new/$', new),
]
