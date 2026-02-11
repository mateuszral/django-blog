from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<int:post_id>/", views.post_details, name="post_details"),
    path("posts/new/", views.new_post, name="new_post"),
]