from django.shortcuts import render, redirect
from .form import PostForm
from datetime import datetime
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, per_page=4)
    page = request.GET.get('page')
    all_posts = paginator.get_page(page)
    return render(request, 'home.html', {'recent_posts': all_posts})

def post(request):
    submitted = False
    form = PostForm
    return render(request, 'post.html', {'form': form})

def author(request):
    return render(request, 'author.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:post')
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})

def detail(request):
    return render(request, 'detail.html')
