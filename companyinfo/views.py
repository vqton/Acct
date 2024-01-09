from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

from .forms import CompanyInformationForm

@login_required
@permission_required('companyinfo.add_companyinformation', 'companyinfo.view_companyinformation')
def index(request):
    if request.method == 'POST':
        form = CompanyInformationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CompanyInformationForm()
    return render(request, 'companyinfo/index.html', {'form': form})
