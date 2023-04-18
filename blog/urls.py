from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<int:blogpost_id>/", views.detail, name="detail"),
    path("blog/", views.all_blogs, name="all_blogs")
]