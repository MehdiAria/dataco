from django.urls import path

from myapp.views import CompanyListView, CompanyListAPIView

urlpatterns = [
    path('list/', CompanyListView.as_view(), name='company-list'), # myapp/views.py
    path('api/corps/', CompanyListAPIView.as_view(), name='company-list-api'), # myapp/views.py

]
