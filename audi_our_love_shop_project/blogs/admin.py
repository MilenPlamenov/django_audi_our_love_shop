from django.contrib import admin

from audi_our_love_shop_project.blogs.models import Blog, Comment


@admin.register(Blog)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    search_fields = ('subject',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()