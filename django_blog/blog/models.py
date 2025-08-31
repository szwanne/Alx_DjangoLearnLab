from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager  # <-- import


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    tags = TaggableManager()  # <-- add this line

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # used by CreateView/UpdateView to redirect to detail page
        return reverse('post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.author.username} on "{self.post.title}"'

    def was_edited(self):
        # helpful in templates to show "edited" label
        return self.updated_at and (self.updated_at - self.created_at).total_seconds() > 1
