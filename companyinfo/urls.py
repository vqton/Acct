from django.urls import path
from .views import index, create, update, delete


app_name = "companyinfo"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create, name="create"),
    path("update/<int:id>/", update, name="update"),
    path("delete/<int:id>/", delete, name="delete"),
]
