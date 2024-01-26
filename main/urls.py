from django.urls import path

from main.apps import MainConfig
from main.views import CurrentUSDRate


app_name = MainConfig.name

urlpatterns = [
    path('get-current-usd/', CurrentUSDRate.as_view(), name='current_usd')
]
