from django.shortcuts import render, get_object_or_404
from .models import Car


# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category='New')  # TODO:Limit the number of cars that appear on a single page
    used_cars = Car.objects.filter(category='Used')
    # To include latest cars
    all = Car.objects.all()

    # TODO: Add custom filter

    return render(request, 'index.html')

    # TODO: Filter results
    # TODO: FilterByCategory


def about(request):
    return render(request, 'about.html')
