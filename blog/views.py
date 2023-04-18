from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from rest_framework import mixins, viewsets
from .serializers import BlogPostSerializer, CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def index(request):
    latest_three_blogs = BlogPost.objects.order_by("-pub_date")[:3]
    return render(request, "blog/index.html", {"latest_three_blogs": latest_three_blogs})

def all_blogs(request):
    blogs = BlogPost.objects.order_by("-pub_date")
    return render(request, "blog/all_blogs.html", {"blogs": blogs})


def detail(request, blogpost_id):
    blog = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = Comment.objects.filter(blog_post=blog)
    return render(request, "blog/blog_detail.html", {"blog": blog, "comments":comments})

# za api
class BlogPostViewSet(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    # ako hocemo sa tokenama
    # authentication_classes = [TokenAuthentication]

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # ako hocemo sa tokenama
    # authentication_classes = [TokenAuthentication]
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]