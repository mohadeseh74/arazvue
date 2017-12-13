from rest_framework import serializers
from request.models import Country, Request

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

# class MethodListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Method
#         fields = '__all__'

class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'sender_country',
        'recipient_country',
        'method',
	'id'
        ]


# class CountryListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
