from django.conf.urls import url
from gallery import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'gallery'




urlpatterns = [
        url(r'^gallery/$', views.GalleryListAPIView.as_view(), name='gallery'),
        ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
