from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<profile_id>\d+)/menu/$', views.Menu.as_view(), name='menu'),
    url(r'^(?P<profile_id>\d+)/start-exercise/$',
        views.StartExercise.as_view(), name='start-exercise'),
    url(r'^(?P<response_session_id>\d+)/summary/$',
        views.ResponseSessionSummary.as_view(), name='summary'),

    url(r'^(?P<response_session_id>\d+)/save-response/$',
        views.SaveResponse.as_view(), name='save-response'),

    url(r'^(?P<profile_id>\d+)/responses-list/$',
        views.ResponsesSession.as_view(), name='responses-list'),

]
