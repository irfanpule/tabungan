from django import forms
from django_select2.forms import ModelSelect2Widget

from sekolah.models import Sekolah
from siswa.models import Siswa
from .models import Debit, Kredit, Tenan
from .utils import get_saldo


class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        fields = ('nominal', 'siswa', 'petugas')
        widgets = {
            'siswa': forms.HiddenInput(),
            'petugas': forms.HiddenInput()
        }


class KreditForm(forms.ModelForm):
    class Meta:
        model = Kredit
        fields = ('nominal', 'siswa', 'petugas')
        widgets = {
            'siswa': forms.HiddenInput(),
            'petugas': forms.HiddenInput()
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)
        if self.instance._state.adding:
            saldo = get_saldo(cleaned_data['siswa'])
            if cleaned_data['nominal'] > saldo:
                raise forms.ValidationError("Nominal yang diinputkan tidak boleh lebih besar dari saldo")
        return cleaned_data


class FilterSiswaAndSekolahForm(forms.Form):
    sekolah = forms.ModelChoiceField(
        queryset=Sekolah.objects.filter(aktif=True),
        widget=ModelSelect2Widget(
            model=Sekolah,
            search_fields=['nama__icontains']
        )
    )
    siswa = forms.ModelChoiceField(
        queryset=Siswa.objects.all(),
        widget=ModelSelect2Widget(
            model=Siswa,
            search_fields=['nama__icontains', 'nis__icontains'],
            dependent_fields={'sekolah': 'sekolah'}
        )
    )


class FilterSiswaForm(forms.Form):
    siswa = forms.ModelChoiceField(
        queryset=Siswa.objects.all(),
        widget=ModelSelect2Widget(
            model=Siswa,
            search_fields=['nama__icontains', 'nis__icontains'],
        ),
        help_text="Masukan Nama siswa atau NIS"
    )


class TenanForm(forms.ModelForm):
    class Meta:
        model = Tenan
        fields = '__all__'
        widgets = {
            'sekolah': ModelSelect2Widget(
                model=Sekolah,
                search_fields=['nama__icontains'],
                help_text="Ketik Nama Sekolah"
            ),
        }
