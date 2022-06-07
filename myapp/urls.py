from django.urls import path

from myapp.views import CompanyListView

urlpatterns = [
    path('list/', CompanyListView.as_view(), name='index-page')
]
