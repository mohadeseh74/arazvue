from rest_framework import generics
from .serializars import (CountryListSerializer,
    RequestCreateSerializer,
    )
from .models import Country, Request


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

# class MethodListAPIView(generics.ListAPIView):
#     queryset = Method.objects.all()
#     serializer_class = MethodListSerializer

class RequestCreateAPIView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestCreateSerializer
