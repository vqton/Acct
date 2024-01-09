from django import forms
from .models import CompanyInformation


class CompanyInformationForm(forms.ModelForm):
    class Meta:
        model = CompanyInformation
        fields = [
            "name",
            "address",
            "city",
            "state",
            "country",
            "zip_code",
            "contact_number",
            "email",
            "tax_identification_number",
            "fiscal_year_start_date",
        ]
