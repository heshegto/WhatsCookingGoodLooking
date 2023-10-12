from django.urls import path
from cooking.views import IndexView, LoginView, SignUpView

app_name = 'cooking'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('sign_up', SignUpView.as_view(), name='sign_up')
]
