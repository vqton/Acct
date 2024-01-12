from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

from .forms import CompanyInformationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyInformationForm
from .models import CompanyInformation


@login_required
@permission_required("companyinfo.view_companyinformation")
def index(request):
    return render(
        request,
        "companyinfo/index.html",
        {"companyinfo_list": CompanyInformation.objects.all()},
    )


@login_required
@permission_required("companyinfo.add_companyinformation")
def create(request):
    if request.method == "POST":
        form = CompanyInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/companyinfo")
    else:
        form = CompanyInformationForm()
    return render(request, "companyinfo/create.html", {"form": form})


@login_required
@permission_required("companyinfo.change_companyinformation")
def update(request, id):
    companyinfo = get_object_or_404(CompanyInformation, pk=id)
    form = CompanyInformationForm(request.POST or None, instance=companyinfo)
    if form.is_valid():
        form.save()
        return redirect("/companyinfo")
    return render(request, "companyinfo/update.html", {"form": form})


@login_required
@permission_required("companyinfo.delete_companyinformation")
def delete(request, id):
    companyinfo = get_object_or_404(CompanyInformation, pk=id)
    companyinfo.delete()
    return redirect("/companyinfo")
