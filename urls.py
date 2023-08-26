from django.urls import path
from . import views

app_name = 'tabungan'
urlpatterns = [
    path('', views.index, name='index'),

    path('debit/list/', views.DebitListView.as_view(), name='debit_list'),
    path('debit/create/', views.DebitCreateView.as_view(), name='debit_create'),
    path('debit/edit/<uuid:id>/', views.DebitUpdateView.as_view(), name='debit_update'),
    path('debit/detail/<uuid:id>/', views.DebitDetailView.as_view(), name='debit_detail'),
    path('debit/delete/<uuid:id>/', views.DebitDeleteView.as_view(), name='debit_delete'),

    path('kredit/list/', views.KreditListView.as_view(), name='kredit_list'),
    path('kredit/create/', views.KreditCreateView.as_view(), name='kredit_create'),
    path('kredit/edit/<uuid:id>/', views.KreditUpdateView.as_view(), name='kredit_update'),
    path('kredit/detail/<uuid:id>/', views.KreditDetailView.as_view(), name='kredit_detail'),
    path('kredit/delete/<uuid:id>/', views.KreditDeleteView.as_view(), name='kredit_delete'),

    path('cek-saldo/', views.CekSaldoView.as_view(), name='cek_saldo'),
]
