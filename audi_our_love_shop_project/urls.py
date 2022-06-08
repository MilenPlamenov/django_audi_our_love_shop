from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('audi_our_love_shop_project.main.urls')),
                  path('users/', include('audi_our_love_shop_project.shop_authentication.urls')),
                  path('contacts/', include('audi_our_love_shop_project.contacts.urls')),
                  path('blog/', include('audi_our_love_shop_project.blogs.urls')),
                  path('shop/', include('audi_our_love_shop_project.shop.urls')),
                  path('payments/', include('audi_our_love_shop_project.payments.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
