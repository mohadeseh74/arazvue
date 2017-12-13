from rest_framework import generics
from .serializer import OurServiceListSerializer, ServiceDetailCreateSerializer
from .models import OurService, ServiceDetail








class OurServiceListAPIView(generics.ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceListSerializer

class ServiceDetailCreateAPIView(generics.ListAPIView):
    queryset = ServiceDetail.objects.all()
    serializer_class = ServiceDetailCreateSerializer
