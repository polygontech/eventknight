from django.conf.urls import url
from . import views

app_name = 'live_event'

urlpatterns = [
    url(r'^$', views.index, name='index'),  # root
    url(r'^submit$', views.submit, name='submit'),
    url(r'^live/(?P<event_id>[0-9]+)$', views.live, name='live'),
]
