from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('cek-saldo/', views.CekSaldoAPIVIew.as_view(), name='api_cek_saldo'),
]
