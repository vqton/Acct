from django.urls import reverse
from django_filters import FilterSet, CharFilter, ChoiceFilter, BooleanFilter
from .models import Account
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit


class UploadFileForm(forms.Form):
    file = forms.FileField()


class AccountFilter(FilterSet):
    # Define the filters for the Account model fields
    # You can use any filter types that suit your needs
    # For example, you can use a CharFilter with a contains lookup for the code and name fields
    # You can use a ChoiceFilter with a list of choices for the level and account_type fields
    # You can use a BooleanFilter for the debit_only field
    code = CharFilter(field_name='code', lookup_expr='icontains')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    level = ChoiceFilter(field_name='level', choices=[
                         (0, '0'), (1, '1'), (2, '2'), (3, '3')])
    account_type = ChoiceFilter(field_name='account_type',
                                choices=[('TÀI SẢN', 'TÀI SẢN'), ('NỢ PHẢI TRẢ', 'NỢ PHẢI TRẢ'),
                                         ('VỐN CHỦ SỞ HỮU',
                                          'VỐN CHỦ SỞ HỮU'), ('DOANH THU', 'DOANH THU'),
                                         ('CHI PHÍ', 'CHI PHÍ')])
    debit_only = BooleanFilter(field_name='debit_only')

    class Meta:
        # Specify the model and the fields to be filtered
        model = Account
        fields = ['code', 'name', 'level', 'account_type', 'debit_only']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'parent_account',
            'code',
            'name',
            'level',
            'account_type',
            'description',
            'opening_balance',
            'debit_only',
            'notes']
