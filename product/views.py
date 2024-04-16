from django.shortcuts import render
from django.core.paginator import Paginator
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

    # Get the number of products per page from request parameters or settings (default to 10)
    # Handles cases where 'per_page' is not in GET
    per_page = int(request.GET.get('per_page', 10))

    # Create a Paginator instance
    paginator = Paginator(products, per_page)

    # Get the current page number from request parameters (default to 1)
    page_number = int(request.GET.get('page', 1))

    # Get the requested page (ensuring it's within valid page range)
    page_obj = paginator.get_page(
        page_number) if page_number <= paginator.num_pages else paginator.page(paginator.num_pages)

    context = {
        'products': page_obj.object_list,
        'paginator': paginator,
        'page_obj': page_obj,
        'per_page': per_page,  # Include per_page for customization in the template
    }

    return render(request, 'product/product_list.html', context)


@login_required  # Add if using authentication
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


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
    return render(request, 'product/product_create.html', context)


@login_required  # Add if using authentication
def product_update(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,
                           instance=product)  # Update existing object
        if form.is_valid():
            form.save()
            # Redirect after update
            return redirect('product/product_detail', product_id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'product/product_update.html', context)


@login_required  # Add if using authentication
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product:product_list')
    context = {'product': product}
    return render(request, 'product/product_delete.html', context)

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
