from django.urls import path
from login.views import *

urlpatterns = [
    path('', login_view , name='login_view'),
    path('register/', register_view, name='register_view'),
    path('home/', home_view, name='home_view'),
    path('profile/', profile_view, name='profile_view'),
    path('update/<int:id>/', update_view, name='update_view'),
    path('delete_account/<int:id>/', delete_account, name='delete_account'),
]
