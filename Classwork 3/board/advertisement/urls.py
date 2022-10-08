from django.urls import path
from .import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement1/', views.advertisement_details, name='advertisement_1'),
    path('contacts/', views.contacts, name='advertisement_contacts'),
    path('about/', views.About.as_view(), name='advertisement_about'),
    path('categories/', views.categories, name='advertisement_categories'),
    path('regions/', views.Regions.as_view(), name='advertisement_regions')
]