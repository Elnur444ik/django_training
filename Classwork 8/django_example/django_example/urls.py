from django.contrib import admin
from django.urls import path
from django.urls import include
from django_example.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('employment/', include('employment.urls'))
]

