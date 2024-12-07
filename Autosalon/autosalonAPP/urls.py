from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('brand/<int:brand_id>/', views.brand_cars, name='brand_cars'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]