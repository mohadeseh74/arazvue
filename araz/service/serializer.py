from rest_framework import serializers
from .models import OurService, ServiceDetail








class OurServiceListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = OurService
        fields = '__all__'

    def get_image(self, obj):
        image = 'http://127.0.0.1:8000'+obj.image.url
        return image

class ServiceDetailCreateSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = ServiceDetail
        fields = '__all__'

    def get_image(self, obj):
        image = 'http://127.0.0.1:8000'+obj.image.url
        return image
