from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower


from .models import Product, Category, Outfit
from .forms import ProductForm, OutfitForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            products = products.order_by(sortkey)
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
                unique_products = set(list(products))
                products = list(unique_products)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def all_outfits(request):
    outfits = Outfit.objects.all()
    products = Product.objects.all()

    if request.GET:
        for products in outfits:
            return products

    context = {
        'outfits': outfits,
        'products': products,
    }

    return render(request, 'products/outfits.html', context)

@login_required
def add_outfit(request):
    """ Add a outfit to the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            Outfit = form.save()
            messages.success(request, 'Successfully added outfit!')
            return redirect(reverse('outfits'))
        else:
            messages.error(request, 'Failed to add outfit. Please ensure the form is valid.')
    else:
        form = OutfitForm()
        
    template = 'products/add_outfit.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def delete_outfit(request, outfit_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    outfit = get_object_or_404(Outfit, pk=outfit_id)
    outfit.delete()
    messages.success(request, 'Outfit deleted!')
    return redirect(reverse('outfits'))

@login_required
def edit_outfit(request, outfit_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    outfit = get_object_or_404(Outfit, pk=outfit_id)
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES, instance=outfit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Outfit!')
            return redirect(reverse('outfits'))
        else:
            messages.error(request, 'Failed to update outfit. Please ensure the form is valid.')
    else:
        form = OutfitForm(instance=outfit)
        messages.info(request, f'You are editing {outfit.name}')

    template = 'products/edit_outfit.html'
    context = {
        'form': form,
        'outfit': outfit,
    }

    return render(request, template, context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        message.error(request, 'Sorry only store owner can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))