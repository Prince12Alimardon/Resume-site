from django.shortcuts import render, redirect
from .models import Post, Comment, Tag
from main.models import Category
from .forms import CommentForm

# Create your views here.


def single_view(request, slug):
    obj = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post__slug=slug)
    tags = Tag.objects.all()
    category = Category.objects.all()
    last_3_posts = Post.objects.order_by('-id')[:3]
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = obj
        comment.save()
        return redirect(f'/posts/single/{obj.slug}#comments')
    ctx = {
        'post': obj,
        'comments': comment,
        'tags': tags,
        'categories': category,
        'last_3_posts': last_3_posts,
        'form': form
    }
    return render(request, 'posts/single.html', ctx)
