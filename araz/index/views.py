from rest_framework import generics
from .serializars import (SliderListSerializer,
    AddressListSerializer,
    PhoneListSerializer,
    StatisticListSerializer,
    OpeningHoursListSerializer,
    SocialNetworksListSerializer,
    NewsletterListSerializer,
    )
from .models import (Slider,
     Address,
     Phone,
     Statistic,
     OpeningHour,
     SocialNetwork,
     Newsletter
     )

class SliderListAPIView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderListSerializer

class AddressListAPIView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer

class PhoneListAPIView(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneListSerializer

class StatisticListAPIView(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticListSerializer

class OpeningHourListAPIView(generics.ListAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHoursListSerializer

class SocialNetworkListAPIView(generics.ListAPIView):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworksListSerializer

class NewsletterCreateAPIView(generics.CreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterListSerializer
