from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

