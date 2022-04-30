
from django.shortcuts import render
from django.views.generic import DetailView

from audi_our_love_shop_project.blogs.forms import CommentForm
from audi_our_love_shop_project.blogs.models import Blog


def blog(request):
    blogs = Blog.objects.all()
    last_blog = blogs.last()
    try:
        all_blogs_without_the_last_blog = Blog.objects.all()[0:len(blogs) - 1]
        context = {
            'blogs': all_blogs_without_the_last_blog,
            'last_blog': last_blog,
            'all_blogs': blogs,
        }
    except ValueError:
        context = {
            'last_blog': last_blog,
            'all_blogs': blogs,
        }
    # could be refactored
    return render(request, 'blogs/blogs.html', context)


class BlogPostDetailsView(DetailView):
    model = Blog
    template_name = "blogs/blog_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


def blog_details(request, pk):
    blog_post = Blog.objects.get(pk=pk)
    blogs = Blog.objects.all()
    comments = blog_post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog_post = blog_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        'object': blog_post,
        'blogs': blogs,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blogs/blog_post.html', context)