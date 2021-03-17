from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Car
from .filters import CarFilter


# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category='New')[:6]
    used_cars = Car.objects.filter(category='Used')[:6]
    latest_cars = Car.objects.all().order_by('-date')[:5]
    all_cars = Car.objects.all()
    custom_filter = CarFilter(request.GET, queryset=all_cars)
    all_cars = custom_filter.qs
    context = {
        'new_cars': new_cars,
        'used_cars': used_cars,
        'latest_cars': latest_cars,
        'all_cars': all_cars,
        'custom_filter': custom_filter
    }

    return render(request, 'index.html', context)

    # TODO: Filter results
    # TODO: FilterByCategory


def about(request):
    return render(request, 'about.html')