from django.shortcuts import render
from products.models import Product
from django.core.paginator import Paginator

# Create your views here.


def index(request):

    new_arrivals = Product.objects.filter(category__name='new_arrivals')
    new_arrivals_list = new_arrivals.all()
    paginator = Paginator(new_arrivals_list, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'new_arrivals': new_arrivals,
        'page_obj': page_obj,
    }

    return render(request, 'home/index.html', context)
