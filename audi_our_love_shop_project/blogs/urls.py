from django.urls import path

from audi_our_love_shop_project.blogs.views import blog, BlogPostDetailsView

urlpatterns = [
    path('', blog, name='blogs'),
    path('post/<int:pk>/', BlogPostDetailsView.as_view(), name='blog post'),
]