from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    return render(request, 'index.html') 

def add_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'add_blog_post.html', {'form': form})

def edit_blog_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('view_blog_posts')
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': form})

def view_blog_posts(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'view_blog_posts.html', {'blog_posts': blog_posts})



