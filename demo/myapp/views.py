from django.shortcuts import render, redirect
from .form import PostForm
from datetime import datetime
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.objects.order_by('-title')
    return render(request, 'home.html', {'recent_posts': all_posts})

def post(request):
    return render(request, 'post.html')

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
