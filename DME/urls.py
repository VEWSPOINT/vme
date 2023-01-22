
from django.contrib import admin
from django.urls import include, path
from Home.views import index_view
from CUA.views import dashboard, customerDash, developerDash, userLogout
from django.conf.urls.static import static
from django.conf import settings

from CUA.views import register
#from Service.views import reportServices_views


urlpatterns = [

    path('', index_view, name='index_view'),
    path('admin/', admin.site.urls),

    path('Contact/', include('Contact.urls')),
    path('Product/', include('Product.urls')),
    path('About/', include('About.urls')),
    path('Payments/', include('Payments.urls')),
    path('Home/', include('Home.urls')),
    path('blog/', include('blog.urls')),
    path('CUA/', include('CUA.urls')),
    path('logout/', userLogout,name='userLogout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customerDash/', customerDash, name='customerDash'),
    path('developerDash/', developerDash, name='developerDash'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
