from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "blog"

router = routers.SimpleRouter()
router.register(r'blogs', views.BlogPostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<int:blogpost_id>/", views.detail, name="detail"),
    path("blog/", views.all_blogs, name="all_blogs"),
    path('api/', include(router.urls))
]