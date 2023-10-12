from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'base.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class SignUpView(TemplateView):
    template_name = 'sign_up.html'
