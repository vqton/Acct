# Assuming you have a form for updating customers
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import CustomerForm
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, DetailView
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .models import Customer
from .forms import CustomerForm  # Assuming you have a form for creating customers


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = '/customers/'  # Redirect to the customer list page


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = '/customers/'  # Redirect to the customer list page


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    # Redirect to the customer list page
    success_url = reverse_lazy('customer-list')
