from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def about(request):
    return render(request, 'about.html')


def filter_results(request):
    display_all = Car.objects.all()
    custom_filter = CarFilter(request.GET, queryset=all)
    display_all = custom_filter.qs
    page = request.GET.get('page')
    paginator = Paginator(display_all, 1)
    try:
        display_all = paginator.page(page)
    except PageNotAnInteger:
        display_all = paginator.page('1')
    except EmptyPage:
        display_all = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page)

    context = {
        'all':display_all,
        'custom_filter':custom_filter,
        'page_obj':page_obj
    }
    return render(request, 'filter_results.html', context)
