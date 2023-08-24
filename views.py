import sweetify
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.mixin import FormFilterMixin
from core.views import (
    ListBreadcrumbView, CreateBreadcrumbView, UpdateBreadcrumbView, BaseDeleteView, DetailBreadcrumbView,
)
from .models import Debit, Kredit
from .forms import DebitForm, KreditForm, FilterSiswaForm
from .utils import get_saldo


@login_required
def index(request):
    return render(request, 'tabungan/index.html')


class DebitListView(ListBreadcrumbView):
    model = Debit
    title_page = 'Data Debit'


class DebitCreateView(FormFilterMixin, CreateBreadcrumbView):
    form_class = DebitForm
    form_filter = FilterSiswaForm
    model = Debit
    template_name = 'tabungan/form_add.html'
    title_page = 'Tambah data debit'
    btn_submit_name = 'Simpan'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        filter_fields = self.get_form_filter_fields()

        if filter_fields.get('sekolah') and filter_fields.get('siswa'):
            kwargs = self.get_form_kwargs()
            filter_fields = self.get_form_filter_fields()
            kwargs['initial']['siswa'] = filter_fields['siswa']
            kwargs['initial']['petugas'] = self.request.user
            return form_class(**kwargs)
        else:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if context.get('siswa'):
            context['saldo'] = get_saldo(context['siswa'])
        context['instruksi'] = "Siswa tersebut ingin melakukan setor tunai sebesar"
        return context

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data debit", timer=5000)
        return reverse('tabungan:debit_list')


class DebitUpdateView(UpdateBreadcrumbView):
    model = Debit
    form_class = DebitForm
    template_name = 'tabungan/form_edit.html'
    title_page = 'Edit data debit'
    btn_submit_name = 'Simpan'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        object = self.get_object()
        context['siswa'] = object.siswa
        context['saldo'] = get_saldo(object.siswa)
        context['instruksi'] = "Petugas ingin melakukan perubahan setor tunai menjadi"
        return context

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


class KreditCreateView(FormFilterMixin, CreateBreadcrumbView):
    form_class = KreditForm
    form_filter = FilterSiswaForm
    model = Kredit
    template_name = 'tabungan/form_add.html'
    title_page = 'Tambah data kredit'
    btn_submit_name = 'Simpan'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        filter_fields = self.get_form_filter_fields()

        if filter_fields.get('sekolah') and filter_fields.get('siswa'):
            kwargs = self.get_form_kwargs()
            filter_fields = self.get_form_filter_fields()
            kwargs['initial']['siswa'] = filter_fields['siswa']
            kwargs['initial']['petugas'] = self.request.user
            return form_class(**kwargs)
        else:
            return None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if context.get('siswa'):
            context['saldo'] = get_saldo(context['siswa'])
        context['instruksi'] = "Siswa tersebut ingin melakukan penarikan tunai sebesar"
        return context

    def get_success_url(self):
        sweetify.toast(self.request, "Berhasil menambahkan data kredit", timer=5000)
        return reverse('tabungan:kredit_list')


class KreditUpdateView(UpdateBreadcrumbView):
    model = Kredit
    form_class = KreditForm
    template_name = 'tabungan/form_edit.html'
    title_page = 'Edit data kredit'
    btn_submit_name = 'Simpan'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        object = self.get_object()
        context['siswa'] = object.siswa
        context['saldo'] = get_saldo(object.siswa)
        context['instruksi'] = "Petugas ingin melakukan perubahan data tarik tunai menjadi"
        return context

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
