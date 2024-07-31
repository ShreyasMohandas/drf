from blog.models import *
from rest_framework import generics
from .serializers import PostSerializer

class PostDetail(generics.RetrieveDestroyAPIView):
    queryset=Post.postobjects.all()
    serializer_class=PostSerializer
    pass

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pass