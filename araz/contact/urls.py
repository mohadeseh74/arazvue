from django.conf.urls import url
from contact import views

app_name = 'contact'

urlpatterns = [
    url(r'^contact_us/$', views.ContactCreate.as_view(), name='contact_us'),
    ]
