# customers/urls.py

from django.urls import path
from . import views
from .views import export_csv_view

app_name = 'customers'  # Optional: Namespace for URL names

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer-list'),
    path('create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('<str:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('<str:pk>/update/', views.CustomerUpdateView.as_view(),
         name='customer_update'),
    path('<str:pk>/delete/', views.CustomerDeleteView.as_view(),
         name='customer-delete'),
    path('export-csv/customers/', export_csv_view, name='export-csv'),
    path('filter/', views.FilterCustomersView.as_view(), name='filter'),

]
