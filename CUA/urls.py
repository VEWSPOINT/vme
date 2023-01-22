from django.urls import path
from CUA.views import register, registerCustomer, registerDeveloper, userLogin, dashboard, customerDash, developerDash
from django.conf.urls.static import static
from django.conf import settings

app_name = 'CUA'

urlpatterns = [
    path('register/', register, name='register'),
    path('registerCustomer/', registerCustomer, name='registerCustomer'),
    path('registerDeveloper/', registerDeveloper, name='registerDeveloper'),
    path('login/', userLogin, name='userLogin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customerDash/', customerDash, name='customerDash'),
    path('developerDash/', developerDash, name='developerDash'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
