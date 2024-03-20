# forms.py

from django import forms
from .models import Customer  # Assuming your Customer model is defined in models.py
from django_ckeditor_5.widgets import CKEditor5Widget


class CustomerForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Customer
        fields = [
            'name',
            'address',
            'phone_number',
            'email',
            'account_balance',
            'credit_limit',
            'tax_id',
            'industry',
            'notes',
        ]

        notes = forms.CharField(widget=CKEditor5Widget(config_name='default'))
    # You can customize form widgets, labels, and validation as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Customize widget attributes
        self.fields['account_balance'].widget.attrs.update(
            {'class': 'form-control'})
        # Example: Change field label
        self.fields['tax_id'].label = 'Tax ID'
        # Add any additional customizations here
