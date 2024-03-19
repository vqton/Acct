from django.db import models
from django.http import HttpResponse
import unicodecsv as csv


class Customer(models.Model):
    """
    Represents a customer (company or similar entity) in the accounting system.
    """

    # Basic information
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Financial details
    account_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    credit_limit = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    # Other relevant fields (you can customize as needed)
    tax_id = models.CharField(
        max_length=20, blank=False, null=False, primary_key=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def export_to_csv():
        """Retrieves all customers, creates a CSV response, writes headers and data rows, and returns the CSV content.
    """
        customers = Customer.objects.all()
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="customer_data.csv"'

        writer = csv.writer(response, encoding='utf-8-sig')
        writer.writerow([
            'Tax ID', 'Name', 'Address', 'Phone Number', 'Email',
            'Account Balance', 'Credit Limit', 'Industry', 'Notes'
        ])

        for customer in customers:
            writer.writerow([
                customer.tax_id, customer.name, customer.address, customer.phone_number, customer.email,
                customer.account_balance, customer.credit_limit, customer.industry, customer.notes
            ])

        return response
