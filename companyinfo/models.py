from django.db import models


class CompanyInformation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    tax_identification_number = models.CharField(max_length=50)
    fiscal_year_start_date = models.DateField()

    class Meta:
        permissions = [
            ("add_companyinfo", "Can add company information"),
            ("change_companyinfo", "Can change company information"),
            ("delete_companyinfo", "Can delete company information"),
            ("view_companyinfo", "Can view company information"),
        ]
