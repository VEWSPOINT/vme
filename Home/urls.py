from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from Home import views






urlpatterns = [


path('', views.index_view, name='index_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)