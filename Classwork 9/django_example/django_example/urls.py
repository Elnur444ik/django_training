from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django_example.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('employment/', include('employment.urls')),
    path('files/', include('app_media.urls')),
    path('files/', include('app_media.urls')),
    path('goods/', include('app_goods.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

