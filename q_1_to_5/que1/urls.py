from django.urls import path
from que1.views import *

urlpatterns = [
    path('', home_view , name='home_view')
]