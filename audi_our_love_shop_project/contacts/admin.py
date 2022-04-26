from django.contrib import admin

from audi_our_love_shop_project.contacts.models import ContactsModel


@admin.register(ContactsModel)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'content')
    search_fields = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()