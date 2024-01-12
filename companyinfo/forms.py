from django import forms
from .models import CompanyInformation
from django.forms.widgets import SelectDateWidget

class CompanyInformationForm(forms.ModelForm):
    fiscal_year_start_date = forms.DateField(
        widget=SelectDateWidget(
            attrs={'class': 'form-control datepicker'}))

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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tax_identification_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
