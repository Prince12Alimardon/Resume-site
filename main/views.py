from django.shortcuts import render, redirect
from person.models import About, Partner, Resume, Project
from posts.models import Post
from .forms import GetInTouchForm
from .models import Service

# Create your views here.


def home_view(request):
    obj = About.objects.order_by('-id')[:1]
    partner = Partner.objects.all()
    post = Post.objects.order_by('-id')
    form = GetInTouchForm(request.POST or None)
    q = request.GET.get('search')
    if q:
        post = post.filter(title__icontains=q)
    cat = request.GET.get('cat')
    if cat:
        post = post.filter(category__category__exact=cat)
    tag = request.GET.get('tag')
    if tag:
        post = post.filter(tag__tag__exact=tag)
    if form.is_valid():
        form.save()
    resume = Resume.objects.all()
    serves = Service.objects.all()
    projects = Project.objects.all()
    ctx = {
        'objects': obj,
        'partners': partner,
        'posts': post,
        'form': form,
        'resume': resume,
        'services': serves,
        'projects': projects
    }
    return render(request, 'index.html', ctx)
