from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^live_event/', include('live_event.urls')),  # import app1 urls
    url(r'^admin/', admin.site.urls),
]