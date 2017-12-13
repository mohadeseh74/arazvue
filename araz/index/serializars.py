from rest_framework import serializers
from index.models import (Slider,
    Address,
    Phone,
    Statistic,
    OpeningHour,
    SocialNetwork,
    Newsletter
    )

class SliderListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Slider
        fields = '__all__'

    def get_image(self, obj):
        image = 'http://127.0.0.1:8000'+obj.image.url
        return image


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

class OpeningHoursListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'

class SocialNetworksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'

class NewsletterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'
