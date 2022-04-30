from django import forms

from audi_our_love_shop_project.blogs.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'rows': '4', 'class': 'form-control'})
        }
