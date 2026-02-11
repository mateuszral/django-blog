from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def posts(request):
    posts_list = Post.objects.order_by("-created_at")
    return render(request, "web_blog/posts.html", {"posts": posts_list})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return HttpResponse(f"<p>{post.title} {post.content} {post.created_at.date()}</p>")
