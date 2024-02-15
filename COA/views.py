from django.urls import reverse_lazy
from .models import Account
from django.views.generic import ListView,CreateView,DetailView, UpdateView, DeleteView
class AccountListView(ListView):
    model = Account
    template_name = 'coa/account_list.html'

class AccountCreateView(CreateView):
    model = Account
    template_name = 'coa/account_create.html'
    fields = ['code', 'name', 'level', 'account_type', 'description', 'opening_balance', 'debit_only', 'parent_account']

class AccountDetailView(DetailView):
    model = Account
    template_name = 'coa/account_detail.html'

class AccountUpdateView(UpdateView):
    model = Account
    template_name = 'coa/account_update.html'
    fields = ['code', 'name', 'level', 'account_type', 'description', 'opening_balance', 'debit_only', 'parent_account']

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'coa/account_delete.html'
    success_url = reverse_lazy('coa:account_list')
