from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('',blog,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('test-',blog_test,name='test'),
]