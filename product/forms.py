from .models import Manufacturer
from .models import Category
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the model

        # Alternatively, specify a subset of fields:
        # fields = ['name', 'description', 'category', 'manufacturer', 'unit_price', 'stock_quantity']

    # Add custom validation or widgets for specific fields if needed (optional)
    image = forms.ImageField(required=False)  # Allow optional image upload
    product_sheet = forms.FileField(
        required=False)  # Allow optional file upload


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'  # Include all fields from the model

        # Alternatively, specify a subset of fields:
        # fields = ['name', 'description', 'parent_category', 'image', 'keywords', 'is_active']

    # Add custom validation or widgets for specific fields if needed (optional)
    image = forms.ImageField(required=False)  # Allow optional image upload


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'  # Include all fields from the model

        # Alternatively, specify a subset of fields:
        # fields = ['name', 'country', 'email', 'phone_number', 'website', 'certifications', 'ethical_practices', 'notes']

    # Add custom validation or widgets for specific fields if needed (optional)
    email = forms.EmailField(required=False)  # Allow optional email
    # Allow optional phone number
    phone_number = forms.CharField(required=False)
