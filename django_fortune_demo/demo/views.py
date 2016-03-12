from django.views.generic import TemplateView


class FortuneView(TemplateView):

    template_name = "fortune.html"
