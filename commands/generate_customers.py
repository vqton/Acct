from django.core.management.base import BaseCommand
from faker import Faker
# Replace ".models" with your app's models path
from customer.models import Customer


class Command(BaseCommand):
    help = 'Generate 100 random Customer objects'

    def handle(self, *args, **options):
        faker = Faker()
        for _ in range(100):
            customer = Customer(
                name=faker.company(),
                address=faker.address().street_address,
                phone_number=faker.phone_number(),
                email=faker.email(),
                account_balance=faker.pydecimal(
                    positive=True, max_digits=8, decimal_places=2),
                credit_limit=faker.pydecimal(
                    positive=True, max_digits=8, decimal_places=2),
                tax_id=faker.unique.ssn(),  # Ensure unique tax id
                industry=faker.industry(),
                notes=faker.text(),
            )
            customer.save()
            self.stdout.write(self.style.SUCCESS(
                f'Created customer: {customer.name}'))
