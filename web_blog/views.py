from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    return render(request, "web_blog/index.html")

def posts(request):
    posts_list = Post.objects.order_by("-created_at")
    return render(request, "web_blog/posts.html", {"posts": posts_list})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.content = post.content
    return render(request, "web_blog/post_details.html", {"post": post})

def new_post(request):
    return render(request, "web_blog/new_post.html")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def login(request):
    return HttpResponse("This is the login page.")
