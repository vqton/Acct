from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Account
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import AccountFilter
from django_filters.views import FilterView
from .forms import AccountForm


class AccountListView(FilterView):
    model = Account
    template_name = 'coa/account_list.html'
    context_object_name = 'accounts'
    filterset_class = AccountFilter


class AccountCreateView(CreateView):
    model = Account
    template_name = 'coa/account_create.html'
    form_class = AccountForm
    # fields = ['code', 'name', 'level', 'account_type', 'description', 'opening_balance', 'debit_only', 'parent_account']

    def form_valid(self, form):
        # get the parent account from the form
        parent_account = form.cleaned_data.get('parent_code')
        # set the debit only field to the same value as the parent account
        form.instance.debit_only = parent_account.debit_only
        # call the super method to save the form
        return super().form_valid(form)


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


def export_csv_view(request):
    return Account.export_to_csv()


def import_csv_view(request):
    from django.shortcuts import render


from .forms import UploadFileForm
from .models import Account


def import_csv_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return HttpResponse(status=400, content='Invalid file type')
            Account.import_from_csv(csv_file)
            return HttpResponse(status=200, content='CSV file imported successfully')
    else:
        form = UploadFileForm()
    return render(request, 'COA/import.html', {'form': form})
