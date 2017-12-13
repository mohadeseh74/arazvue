from django.conf.urls import url
from index import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'index'

urlpatterns = [
    url(r'^slider/$', views.SliderListAPIView.as_view(), name='slider'),
    url(r'^address/$', views.AddressListAPIView.as_view(), name='address'),
    url(r'^phone/$', views.PhoneListAPIView.as_view(), name='phone'),
    url(r'^statistic/$', views.StatisticListAPIView.as_view(), name='statistic'),
    url(r'^opening_hour/$', views.OpeningHourListAPIView.as_view(), name='opening_hour'),
    url(r'^social_network/$', views.SocialNetworkListAPIView.as_view(), name='social_network'),
    url(r'^newsletter/$', views.NewsletterCreateAPIView.as_view(), name='newsletter'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
