from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from myapp.models import Company, Esg
from myapp.serializer import CompanySerializer, EsgSerializer


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


from django.shortcuts import get_object_or_404


class EsgDetailsView(DetailView):
    model = Esg
    template_name = 'esg_detail.html'
    context_object_name = 'items'
    slug_field = 'ricCode'
    slug_url_kwarg = 'code'
    # def setup(self, request, *args, **kwargs):
    #     esg_instance = get_object_or_404(Esg, ricCode=kwargs['code'])
    #     # print('A' * 50, esg_instance)
    #     return super().setup(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)
    # slug_url_kwarg = 'ricCode'
    # context_object_name = 'slug'


class EsgDetailsAPIView(RetrieveAPIView):
    serializer_class = EsgSerializer
    queryset = Esg.objects.all()
    lookup_field = 'ricCode'
    lookup_url_kwarg = 'code'
