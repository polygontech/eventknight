from django.conf.urls import url
from . import views

app_name = 'ek_engine'

urlpatterns = [
    url(r'^$', views.fire_up_ek_engine, name='fire_up_ek_engine'),
]
