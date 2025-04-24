from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"

class LoginPageView(TemplateView):
    template_name = "pages/login.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
