from django.urls import path, include
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

    path('tenan/list/', views.TenanListView.as_view(), name='tenan_list'),
    path('tenan/create/', views.TenanCreateView.as_view(), name='tenan_create'),
    path('tenan/edit/<uuid:id>/', views.TenanUpdateView.as_view(), name='tenan_update'),
    path('tenan/detail/<uuid:id>/', views.TenanDetailView.as_view(), name='tenan_detail'),
    path('tenan/delete/<uuid:id>/', views.TenanDeleteView.as_view(), name='tenan_delete'),

    path('api/', include('addons.tabungan.api.urls'))
]
