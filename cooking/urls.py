from django.urls import path
from cooking.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]