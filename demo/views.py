from django.views.generic import TemplateView


class FortuneDemoView(TemplateView):

    template_name = "fortune_demo.html"
