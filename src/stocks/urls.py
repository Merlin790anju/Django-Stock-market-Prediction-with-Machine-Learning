from django.urls import path
from stocks.views import *

urlpatterns = [
    path('', index),
    path('search/', search),
    path('predict/<str:ticker_value>/<str:number_of_days>/', predict),
    path('ticker/', ticker),
]