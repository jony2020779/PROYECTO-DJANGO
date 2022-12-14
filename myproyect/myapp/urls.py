from django.urls import path, include
from .views import Blog

app_name="blog"
urlpatterns = [
    path('',Blog.as_view(),name="blog_home"),
]