from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from .models import Post, Like
from rest_framework import generics
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')
        feed_data = [
            {
                "id": posts.id,
                "author": posts.author.username,
                "title": posts.title,
                "content": posts.content,
                "created_at": posts.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(
            author__in=following_users).order_by('-created_at')
        feed_data = [
            {
                "id": posts.id,
                "author": posts.author.username,
                "title": posts.title,
                "content": posts.content,
                "created_at": posts.created_at,
            }
            for post in posts
        ]
        return Response(feed_data)


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)

        if like.exists():
            like.delete()
            return Response({'message': 'Post unliked successfully!'})
        else:
            return Response({'message': 'You have not liked this post yet.'}, status=400)
