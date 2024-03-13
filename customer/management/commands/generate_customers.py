from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import DynamicProvider
# Replace ".models" with your app's models path
from customer.models import Customer


class Command(BaseCommand):
    help = 'Generate 100 random Customer objects'

    def handle(self, *args, **options):
        faker = Faker()
        industries = DynamicProvider(
            provider_name="industries",
            elements=["Pharmaceuticals and Healthcare",
                      "Automotive and Energy",
                      "Consumer Goods and Technology",
                      "Oil and Gas Exploration",
                      "Automotive and Manufacturing",
                      "Technology and Internet", "Financial Services and Banking", "Energy and Oil"],
        )
        faker.add_provider(industries)

        for _ in range(100):
            customer = Customer(
                name=faker.company(),
                address=faker.street_address(),
                phone_number=faker.phone_number()[:20],
                email=faker.email(),
                account_balance=faker.pydecimal(
                    left_digits=5, right_digits=2, positive=True),
                credit_limit=faker.pydecimal(
                    left_digits=5, right_digits=2, positive=True),
                tax_id=faker.unique.ssn(),  # Ensure unique tax id
                industry=faker.industries(),
                notes=faker.text(),
            )
            customer.save()
            self.stdout.write(self.style.SUCCESS(
                f'Created customer: {customer.name}'))
