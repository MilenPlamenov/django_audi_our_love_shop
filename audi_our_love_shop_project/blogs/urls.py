from django.urls import path

from audi_our_love_shop_project.blogs.views import blog, BlogPostDetailsView, blog_details, BlogsSearch

urlpatterns = [
    path('', blog, name='blogs'),
    path('post/<int:pk>/', blog_details, name='blog post'),
    path('searched-blogs/', BlogsSearch.as_view(), name='searched-blogs'),
]
