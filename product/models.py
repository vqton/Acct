from django.db import models


class Product(models.Model):
    # Basic product information
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)

    # Pricing and inventory
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    # Product media (images, files, etc.)
    image = models.ImageField(
        upload_to='product_images/', null=True, blank=True)
    product_sheet = models.FileField(
        upload_to='product_sheets/', null=True, blank=True)

    # Additional attributes (customize as needed)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    parent_category = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='category_images/', null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # Add custom attributes as needed (e.g., color, screen size)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)
    ethical_practices = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
