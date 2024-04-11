from django.shortcuts import render
from .models import Product, Category, Manufacturer
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
# Add if using user authentication
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, CategoryForm, ManufacturerForm  # Import your forms

# Product Views


@login_required  # Add if using authentication
def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


@login_required  # Add if using authentication
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


@login_required  # Add if using authentication
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            # Redirect after successful creation
            return redirect('product_list')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'product_create.html', context)


@login_required  # Add if using authentication
def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,
                           instance=product)  # Update existing object
        if form.is_valid():
            form.save()
            # Redirect after update
            return redirect('product_detail', product_id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'product_update.html', context)


@login_required  # Add if using authentication
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    context = {'product': product}
    return render(request, 'product_delete.html', context)

# Category Views (similar structure as product views)


def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category_list.html', context)


def category_detail(request, category_id):
    # ...
    pass


def category_create(request):
    # ...
    pass


def category_update(request, category_id):
    # ...
    pass


def category_delete(request, category_id):
    # ...
    pass
    # Manufacturer Views (similar structure as product views)


def manufacturer_list(request):
    # ...
    pass


def manufacturer_detail(request, manufacturer_id):
    # ...
    pass


def manufacturer_create(request):
    # ...
    pass


def manufacturer_update(request, manufacturer_id):
    # ...
    pass


def manufacturer_delete(request, manufacturer_id):
    # ...
    pass
