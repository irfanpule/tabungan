import sweetify
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView,
)
from .models import Debit, Kredit
from .forms import DebitForm, KreditForm


@login_required
def index(request):
    return render(request, 'tabungan/index.html')


class DebitListView(ListBreadcrumbView):
    model = Debit
    title_page = 'Data Debit'


class DebitCreateView(CreateBreadcrumbView):
    form_class = DebitForm
    model = Debit
    template_name = 'tabungan/form.html'
    title_page = 'Tambah data debit'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data debit", timer=5000)
        return reverse('tabungan:debit_list')


class DebitUpdateView(UpdateBreadcrumbView):
    model = Debit
    form_class = DebitForm
    template_name = 'tabungan/form.html'
    title_page = 'Edit data debit'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data debit", timer=5000)
        return reverse('tabungan:debit_list')


class DebitDetailView(DetailBreadcrumbView):
    model = Debit
    template_name = 'tabungan/general_detail.html'

    def get_title_page(self):
        return "Detail Debit"


class DebitDeleteView(BaseDeleteView):
    model = Debit

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data debit", timer=5000)
        return reverse('tabungan:debit_list')


class KreditListView(ListBreadcrumbView):
    model = Kredit
    title_page = 'Data Kredit'


class KreditCreateView(CreateBreadcrumbView):
    form_class = KreditForm
    model = Kredit
    template_name = 'tabungan/form.html'
    title_page = 'Tambah data kredit'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kredit", timer=5000)
        return reverse('tabungan:kredit_list')


class KreditUpdateView(UpdateBreadcrumbView):
    model = Kredit
    form_class = KreditForm
    template_name = 'tabungan/form.html'
    title_page = 'Edit data kredit'
    btn_submit_name = 'Simpan'

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil mengubah data kredit", timer=5000)
        return reverse('tabungan:kredit_list')


class KreditDetailView(DetailBreadcrumbView):
    model = Kredit
    template_name = 'tabungan/general_detail.html'

    def get_title_page(self):
        return "Detail Kredit"


class KreditDeleteView(BaseDeleteView):
    model = Kredit

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menghapus data kredit", timer=5000)
        return reverse('tabungan:kredit_list')
