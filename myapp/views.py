from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from myapp.models import Company
from myapp.serializer import CompanySerializer


class CompanyListView(ListView):
    model = Company
    queryset = Company.objects.all()
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        company_list = Company.objects.all()
        context = {'company_list': company_list}
        return render(request, 'company_list.html', context=context)


class CustomNumberPagination(PageNumberPagination):
    page_size = 10


class CompanyListAPIView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    pagination_class = CustomNumberPagination
