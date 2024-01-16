from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):

    new_arrivals = Product.objects.filter(category__name='new_arrivals')

    context = {
        'new_arrivals': new_arrivals,
    }

    return render(request, 'home/index.html', context)
