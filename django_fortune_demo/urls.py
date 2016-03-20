from django.conf.urls import include, url

from demo.views import FortuneDemoView


urlpatterns = [url(r"^$",
                   FortuneDemoView.as_view(),
                   name="fortune-demo"),
               url(r"^fortune/",
                   include("fortune.urls",
                           namespace="fortune"))]
