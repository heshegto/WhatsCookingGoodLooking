from django.urls import path
from cooking.views import IndexView

app_name = 'cooking'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]