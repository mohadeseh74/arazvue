from rest_framework import serializers
from .models import Gallery










class GalleryListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Gallery
        fields = '__all__'

    def get_image(self, obj):
      try:
        image = 'http://144.76.233.153:8000' + obj.image.url
      except:
        image = None
      return image
