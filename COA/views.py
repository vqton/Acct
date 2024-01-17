# Create your views here.

# views.py
import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import AccountCategory, Account, SubAccount


def index(request):
    return render(request,'COA/index.html')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="account_data.csv"'

    writer = csv.writer(response)
    
    # Write header row
    writer.writerow(['Category Name', 'Category Description'])
    
    # Write data for AccountCategory model
    for category in AccountCategory.objects.all():
        writer.writerow([category.name, category.description])

    # Add a blank line
    writer.writerow([])

    # Write header row for Account model
    writer.writerow(['Category', 'Code', 'Name', 'Description', 'Account Type', 'Parent Account'])

    # Write data for Account model
    for account in Account.objects.all():
        writer.writerow([
            account.category.name,
            account.code,
            account.name,
            account.description,
            account.account_type,
            account.parent_account.code if account.parent_account else ''
        ])

    # Add a blank line
    writer.writerow([])

    # Write header row for SubAccount model
    writer.writerow(['Account Code', 'Code', 'Name', 'Description'])

    # Write data for SubAccount model
    for subaccount in SubAccount.objects.all():
        writer.writerow([
            subaccount.account.code,
            subaccount.code,
            subaccount.name,
            subaccount.description
        ])

    return response
