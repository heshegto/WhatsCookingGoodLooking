from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from user.mixins import TitleMixin
from user.forms import UserLoginForm, UserRegistrationForm
from user.models import User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('cooking:index')
    title = 'Login'


class SignUpView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/sign_up.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = "Successful Sign up!"
    title = 'Sign up'

