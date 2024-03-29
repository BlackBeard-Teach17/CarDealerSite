from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from .filters import CarFilter
from dealers.models import Dealer


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


def about(request):
    return render(request, 'about.html')


def filter_results(request):
    all_cars = Car.objects.all()
    custom_filter = CarFilter(request.GET, queryset=all)
    all_cars = custom_filter.qs
    page = request.GET.get('page')
    paginator = Paginator(all_cars, 1)
    try:
        all_cars = paginator.page(page)
    except PageNotAnInteger:
        all_cars = paginator.page('1')
    except EmptyPage:
        all_cars = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page)

    context = {
        'all_cars': all_cars,
        'custom_filter': custom_filter,
        'page_obj': page_obj
    }
    return render(request, 'filter_results.html', context)


def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars': cars
    }

    render(request, 'car_detail.html', context)


def inventory(request):
    car_inventory = Car.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(car_inventory, 5)
    try:
        car_inventory = paginator.page(page)
    except PageNotAnInteger:
        car_inventory = paginator.page('1')
    except EmptyPage:
        car_inventory = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page)
    context = {
        'car_inventory': car_inventory,
        'page_obj': page_obj
    }

    return render(request, 'inventory.html', context)


def dealers(request):
    all_dealers = Dealer.objects.all()
    context = {
        'all_dealers': all_dealers
    }
    return render(request, 'dealers.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Question from' + name + ' Email ' + email,
            message,
            email,
            ['']
        )
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')
