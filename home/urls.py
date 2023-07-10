from django.urls import path
from .views import IndexView, TransactionView, generate_qr

urlpatterns = [
    path('', IndexView),
    path('transactions', TransactionView),
    path('qr', generate_qr),
]