from django.shortcuts import render
from .models import Brand, Car

def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    return render(request, 'home.html', {'brands': brands, 'cars': cars})

def brand_cars(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand=brand)
    return render(request, 'brand_cars.html', {'brand': brand, 'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'car_detail.html', {'car': car})