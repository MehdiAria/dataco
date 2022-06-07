from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from myapp.models import Company
from myapp.serializer import CompanySerializer


class CompanyListView(ListView):
    """View to list all companies"""
    model = Company
    queryset = Company.objects.all()
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        company_list = Company.objects.all()
        context = {'company_list': company_list}
        return render(request, 'company_list.html', context=context)


class CustomNumberPagination(PageNumberPagination):
    """Custom pagination"""
    page_size = 10


class CompanyListAPIView(ListAPIView):
    """List API view with authentication"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    pagination_class = CustomNumberPagination
    permission_classes = [IsAuthenticated]

# TODO
# class EsgDetailsView(DetailView):
#     model = Esg
#     template_name = 'esg_detail.html'
