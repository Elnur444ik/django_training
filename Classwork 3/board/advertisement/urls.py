from django.urls import path
from .import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement1/', views.advertisement_details, name='advertisement_list'),
    path('contacts/', views.contacts, name='advertisement_list'),
    path('about/', views.About.as_view(), name='advertisement_list'),
    path('categories/', views.categories, name='advertisement_list'),
    path('regions/', views.Regions.as_view(), name='advertisements_list')
]