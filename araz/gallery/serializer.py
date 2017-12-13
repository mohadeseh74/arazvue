from rest_framework import serializers
from .models import Gallery










class GalleryListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Gallery
        fields = '__all__'

    def get_image(self, obj):
        image = 'http://127.0.0.1:8000'+obj.image.url
        return image
