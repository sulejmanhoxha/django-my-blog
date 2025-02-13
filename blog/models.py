from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe 

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    picture =  models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.picture))

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.content}"
