from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import RegisterUserForm, UpdateProfileForm, UpdateUserForm


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


class ProfileView(UpdateView):

    template_name = "pages/profile.html"
    title = 'Profile'
    success_url = reverse_lazy('MCIW:profile')
    fields = ['username']
    form = UpdateUserForm

    def get_object(self):
        return self.request.user


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['title'] = self.title
        return context

    