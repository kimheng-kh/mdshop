from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product, Banner



def index(request):
    banners= Banner.objects.all()
    products= Product.objects.order_by('-date').filter(is_publish=True)[:6]
    context={
        'banners':banners,
        'products':products
    }
    return render(request, 'index.html', context)



def products(request):
    products= Product.objects.order_by('-date').filter(is_publish=True)
    paginator=Paginator(products, 12)
    page= request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'products':paged_listings
    }
    return render(request, 'products.html', context)


def about(request):
    
    return render(request, 'about.html')



