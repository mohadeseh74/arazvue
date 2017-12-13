from django.conf.urls import url
from service import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'service'

urlpatterns = [
    url(r'^our_service/$', views.OurServiceListAPIView.as_view(), name='our_service'),
    url(r'^service/$', views.ServiceDetailCreateAPIView.as_view(), name='service_detail'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
