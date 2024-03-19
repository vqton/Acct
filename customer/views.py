# Assuming you have a form for updating customers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from .forms import CustomerForm
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Customer
from .forms import CustomerForm  # Assuming you have a form for creating customers


def export_csv_view(request):
    return Customer.export_to_csv()


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customers:customer-list')


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10  # Set the number of customers per page

    def get_queryset(self):
        # Order the queryset by a specific field (e.g., 'last_name')
        return super().get_queryset().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        # Get the current page number from the URL
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'customer'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = '/customers/'  # Redirect to the customer list page


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customer/customer_confirm_delete.html'
    # Redirect to the customer list page
    success_url = reverse_lazy('customers:customer-list')
