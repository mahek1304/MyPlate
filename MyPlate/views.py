from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class LoggedIn(TemplateView):
    template_name = 'loggedin.html'

    



