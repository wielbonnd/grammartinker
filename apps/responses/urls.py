from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<profile_id>\d+)/menu/$', views.Menu.as_view(), name='menu'),
    url(r'^(?P<profile_id>\d+)/start-exercise/$',
        views.StartExercise.as_view(), name='start-exercise'),

    url(r'^(?P<response_session_id>\d+)/summary/$',
        views.ResponseSessionSummary.as_view(), name='summary'),
]
