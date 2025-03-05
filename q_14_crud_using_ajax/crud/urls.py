from django.urls import path
from .views import *

urlpatterns = [
    path('', blogs_view, name='blogs_view'),
    path('create_blog/', create_blog, name='create_blog'),
    path('delete/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog'),
]