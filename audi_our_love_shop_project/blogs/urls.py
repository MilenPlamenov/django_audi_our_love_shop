from django.urls import path

from audi_our_love_shop_project.blogs.views import blog

urlpatterns = [
    path('', blog, name='blogs'),
]