from django.urls import path

from myapp.views import CompanyListView, CompanyListAPIView, EsgDetailsView, EsgDetailsAPIView

urlpatterns = [
    path('list/', CompanyListView.as_view(), name='company-list'),  # myapp/views.py
    path('detail/<slug:code>', EsgDetailsView.as_view(), name='company-detail'),  # myapp/views.py
    path('api/corps/', CompanyListAPIView.as_view(), name='company-list-api'),  # myapp/views.py
    path('api/corps/esgscore/<slug:code>', EsgDetailsAPIView.as_view(), name='company-detail-api'),  # myapp/views.py

]
