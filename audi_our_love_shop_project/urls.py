from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('audi_our_love_shop_project.main.urls')),
    path('users/', include('audi_our_love_shop_project.shop_authentication.urls')),
    path('contacts/', include('audi_our_love_shop_project.contacts.urls')),
]
