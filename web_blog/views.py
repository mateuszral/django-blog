from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def post_list(request):
    return HttpResponse("This is the list of blog posts.")

def post_detail(request, post_id):
    return HttpResponse(f"This is the detail of post {post_id}.")
