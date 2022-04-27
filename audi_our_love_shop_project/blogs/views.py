from django.shortcuts import render

from audi_our_love_shop_project.blogs.models import Blog


def blog(request):
    blogs = Blog.objects.all()
    last_blog = blogs.last()
    all_blogs_without_the_last_blog = Blog.objects.all()[0:len(blogs) - 1]
    context = {
        'blogs': all_blogs_without_the_last_blog,
        'last_blog': last_blog,
    }
    return render(request, 'blogs/blogs.html', context)
