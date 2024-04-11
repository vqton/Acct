from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import DynamicProvider, BaseProvider
from product.models import Product, Category, Manufacturer
import random


class ProductNameProvider(BaseProvider):
    def __init__(self, generator):  # Add the 'generator' argument
        super().__init__(generator)  # Call the base class constructor

    def product_name(self):
        nouns = ["Widget", "Gadget", "Tool", "Appliance", "Machine"]
        adjectives = ["Smart", "Eco-Friendly",
                      "Heavy-Duty", "Portable", "Luxury"]
        return f"{random.choice(adjectives)} {random.choice(nouns)} {self.numerify('###')}"


class Command(BaseCommand):
    help = 'Generates fake data for Product, Category, and Manufacturer models.'

    def handle(self, *args, **options):
        fake = Faker()
        # Pass the 'fake' instance as the generator argument
        fake.add_provider(ProductNameProvider(fake))
        # Generate Category data
        categories = []
        for _ in range(100):
            name = fake.company()
            description = fake.text()
            parent_category = random.choice(categories) if categories else None
            category = Category.objects.create(
                name=name, description=description, parent_category=parent_category
            )
            categories.append(category)

        # Generate Manufacturer data
        manufacturers = []
        for _ in range(100):
            name = fake.company()
            country = fake.country()
            email = fake.email()
            website = fake.url()
            manufacturer = Manufacturer.objects.create(
                name=name, country=country, email=email, website=website
            )
            manufacturers.append(manufacturer)

        # Generate Product data
        for _ in range(100):
            name = fake.product_name()
            description = fake.text()
            category = random.choice(categories)
            manufacturer = random.choice(manufacturers)
            # Generate random price
            unit_price = round(random.uniform(10, 100), 2)
            stock_quantity = random.randint(1, 100)  # Generate random stock
            product = Product.objects.create(
                name=name, description=description, category=category,
                manufacturer=manufacturer, unit_price=unit_price, stock_quantity=stock_quantity
            )

        self.stdout.write(self.style.SUCCESS(
            'Successfully generated 100 rows of fake data for each model.'))
