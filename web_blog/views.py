from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .models import Post
from .forms import PostForm


def home(request):
    return render(request, "web_blog/home.html")

def posts(request):
    posts_list = Post.objects.order_by("-created_at")
    return render(request, "web_blog/posts.html", {"posts": posts_list})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.content = post.content
    return render(request, "web_blog/post_details.html", {"post": post})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.get_username()
            post.save()
            return redirect("post_details", post_id=post.id)
        
    form = PostForm()
    return render(request, "web_blog/new_post.html", {"form": form})

def about(request):
    return render(request, "web_blog/about.html")

def contact(request):
    return render(request, "web_blog/contact.html")

def login(request):
    return HttpResponse("This is the login page.")

def logout(request):
    request.session.flush()
    return redirect("")

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_details", post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "web_blog/edit_post.html", {"form": form, "post": post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect("posts")