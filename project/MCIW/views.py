from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from .forms import RegisterUserForm


class HomeView(TemplateView):
    template_name = "pages/dashboard.html"
    title = 'MCIW'
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class RegisterView(TemplateView):
    
    template_name = "pages/register.html"
    form = RegisterUserForm
    title = 'Inscription'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("MCIW:login")



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['title'] = self.title
        return context