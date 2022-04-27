from django.contrib import admin

from audi_our_love_shop_project.blogs.models import Blog


@admin.register(Blog)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ('subject',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
