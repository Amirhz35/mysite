from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('blog',blog,name='index'),
    path('blog/single',blog_single,name='single'),
]