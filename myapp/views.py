from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from myapp.models import Company


class CompanyListView(ListView):
    model = Company
    queryset = Company.objects.all()
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        company_list = Company.objects.all()
        context = {'company_list': company_list}
        return render(request, 'company_list.html', context=context)
