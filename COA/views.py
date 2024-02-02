# Create your views here.

# views.py
import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import  Account


def index(request):
    return render(request,'COA/index.html')

def import_account_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            account = Account(
                account_code=int(row['account_code']),
                account_name=row['account_name'],
                account_type=int(row['account_type']),
                account_group=int(row['account_group']),
                account_content=row['account_content'],
                accounting_method=row['accounting_method']
            )
            account.save()
    