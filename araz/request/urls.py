from django.conf.urls import url, include
from request import views
from rest_framework import routers

router = routers.SimpleRouter()

app_name = 'request'

urlpatterns = [
    url(r'^request/$', views.RequestCreateAPIView.as_view(), name='create_request'),
    # url(r'^country/$', views.CountryListAPIView.as_view(), name='country_list'),
    # url(r'^method/$', views.MethodListAPIView.as_view(), name='method_list'),
    url(r'^', include(router.urls)),
]
