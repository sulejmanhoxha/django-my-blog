from django.contrib import admin
from .models import BlogPost, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Author information", {"fields": ["author", "author_name"]}),
        ("Blog content", {"fields": ["title", "picture", "content"]}),
    ]

    inlines = [CommentInline]
	
    list_display = ["author_name","image_tag", "pub_date", "title"]
    list_filter = ["pub_date", "author_name", "title"]
    search_fields = ["title"]

class CommentAdmin(admin.ModelAdmin): 
    list_display = ["user", "blog_post", "pub_date"]
    list_filter = ["user", "blog_post"]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)