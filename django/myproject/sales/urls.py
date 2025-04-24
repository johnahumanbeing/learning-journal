from django.urls import path
from .views import register_employee, record_sale, sales_report

urlpatterns = [
    path('register/', register_employee, name='register_employee'),
    path('record-sale/', record_sale, name='record_sale'),
    path('sales-report/', sales_report, name='sales_report'),
]
