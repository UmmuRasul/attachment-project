from rest_framework import routers
from .api import PostViewSet, ContactUsViewSet, NewsViewSet, VideoViewSet

routers = routers.DefaultRouter()
routers.register('api/post', PostViewSet, 'post')
routers.register('api/news', NewsViewSet, 'news')
routers.register('api/video', VideoViewSet, 'video')
routers.register('api/contactus', ContactUsViewSet, 'contactus')

urlpatterns = routers.urls
