from django.urls import path
from . import views  # Import views from the same directory (usually)

app_name = 'product'

urlpatterns = [
    # Products
    path('', views.product_list, name='product_list'),  # List all products
    # Detail view for a specific product
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # Create a new product
    path('add/', views.product_create, name='product_create'),
    path('update/<int:product_id>/', views.product_update,
         name='product_update'),  # Update an existing product
    path('delete/<int:product_id>/', views.product_delete,
         name='product_delete'),  # Delete a product

    # Categories
    path('categories/', views.category_list,
         name='category_list'),  # List all categories
    path('categories/<int:category_id>/', views.category_detail,
         name='category_detail'),  # Detail view for a category
    path('categories/add/', views.category_create,
         name='category_create'),  # Create a new category
    path('categories/update/<int:category_id>/', views.category_update,
         name='category_update'),  # Update a category
    path('categories/delete/<int:category_id>/', views.category_delete,
         name='category_delete'),  # Delete a category

    # Manufacturers
    path('manufacturers/', views.manufacturer_list,
         name='manufacturer_list'),  # List all manufacturers
    path('manufacturers/<int:manufacturer_id>/', views.manufacturer_detail,
         name='manufacturer_detail'),  # Detail view for a manufacturer
    path('manufacturers/add/', views.manufacturer_create,
         name='manufacturer_create'),  # Create a new manufacturer
    path('manufacturers/update/<int:manufacturer_id>/', views.manufacturer_update,
         name='manufacturer_update'),  # Update a manufacturer
    path('manufacturers/delete/<int:manufacturer_id>/', views.manufacturer_delete,
         name='manufacturer_delete'),  # Delete a manufacturer
]
