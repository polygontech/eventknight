from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('base.urls')),
    url(r'^events/', include('live_event.urls')),  # import app1 urls
    url(r'^ekengine/', include('eventknight_engine.urls')),  # import app1 urls
    url(r'^admin/', admin.site.urls),
]