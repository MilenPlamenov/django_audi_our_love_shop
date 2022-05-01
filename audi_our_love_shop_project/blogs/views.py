from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from audi_our_love_shop_project.blogs.forms import CommentForm
from audi_our_love_shop_project.blogs.models import Blog, Comment


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


# most of the code from stackoverflow
def blog_details(request, pk):
    blog_post = Blog.objects.get(pk=pk)
    blogs = Blog.objects.all()
    comments = blog_post.comments.filter(parent__isnull=True)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj

            comment = comment_form.save(commit=False)
            comment.blog_post = blog_post
            comment.blog_id = blog_post.id
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        if request.user.is_authenticated:
            comment_form = CommentForm(initial={'email': request.user.email})
        else:
            comment_form = CommentForm()

    context = {
        'object': blog_post,
        'blogs': blogs,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blogs/blog_post.html', context)
