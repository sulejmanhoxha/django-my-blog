from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment


def index(request):
    latest_three_blogs = BlogPost.objects.order_by("-pub_date")[:3]
    return render(request, "blog/index.html", {"latest_three_blogs": latest_three_blogs})

def all_blogs(request):
    blogs = BlogPost.objects.all()
    return render(request, "blog/all_blogs.html", {"blogs": blogs})


def detail(request, blogpost_id):
    blog = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = Comment.objects.filter(blog_post=blog)
    return render(request, "blog/blog_detail.html", {"blog": blog, "comments":comments})
