from django.urls import path
from developer.views import *


urlpatterns = [
    path('', home_view ,name='home'),
    path('developer/', developer_list_view , name='developer_list_view'),
    path('contact/', contact_view , name= 'contact_view'),
    path('register/',register_view , name='register_view'),

]

