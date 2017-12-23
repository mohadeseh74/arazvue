from rest_framework import serializers
from request.models import Request

# class CountryListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = '__all__'

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
        'sender',
        'recipient',
        'goods_type',
        'weight',
        'dimentions',
        'phone_number',
        'email',
        'method',
	'id'
        ]


# class CountryListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Country
