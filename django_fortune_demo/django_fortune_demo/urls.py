from django.conf.urls import include, url
from django.contrib import admin

from demo.views import FortuneView


urlpatterns = [url(r'^$', FortuneView.as_view()),
               url(r'^admin/', admin.site.urls),
               url(r'^api/', include('fortune.urls', namespace='api'))]
