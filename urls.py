from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('apps.profiles.urls', namespace="profiles")),
    url(r'^responses/', include('apps.responses.urls', namespace="responses")),
]
