# forms.py

from django import forms
from .models import Customer  # Assuming your Customer model is defined in models.py
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number',
                  'tax_id']  # Customize fields for update


class CustomerForm(forms.ModelForm):

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
        widgets = {
            'notes': SummernoteWidget(),

        }
    # You can customize form widgets, labels, and validation as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Customize widget attributes
        self.fields['account_balance'].widget.attrs.update(
            {'class': 'form-control'})
        # Example: Change field label
        self.fields['tax_id'].label = 'Tax ID'
        # Add any additional customizations here
