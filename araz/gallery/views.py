from rest_framework import generics
from .serializer import GalleryListSerializer
from .models import Gallery






class GalleryListAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryListSerializer
