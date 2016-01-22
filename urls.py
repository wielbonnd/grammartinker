from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='profiles:profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profiles/', include('apps.profiles.urls', namespace="profiles")),
    url(r'^responses/', include('apps.responses.urls', namespace="responses")),
    url(r'^verbs/', include('apps.verbs.urls', namespace="verbs")),
]
