from videonews.models import Post, News, Video, ContactUs
from rest_framework import viewsets, permissions
from .serializers import PostSerializer, NewsSerializer, VideoSerializer, ContactUsSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = VideoSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    permissions_class = [
        permissions.AllowAny
    ]
    serializer_class = ContactUsSerializer
