# Tabungan
Tabungan ada addons xyacad untuk manajemen Tabungan sekolah

## Cara installl
- symlink atau copas atau clone addons project ini ke dalam `xyacad/addons/`
- setelah itu registrasikan addons tsb pada local settings
```
INSTALLED_ADDONS = [
    .... # addons lainnya
    'addons.tabungan'
]
``` 
- setelah itu kamu bisa menjalankan command manage.py terhadap addons yang sudah ditambahkan. Misal `python manage.py migrate tabungan`

## Membuat Addons Xyacad
Pada dasarnya addons xyacad adalah app django biasa yang ditambahkan manifest pada `__init__.py` app django. Contoh
```python
# detail attribute for addons apps
short_desc = "Tabungan Sekolah"  # deskripsi singkat
icon = "fa fa-money-bill"  # mengacu pada class fontawesome
color = "red"  # warna background pada card addons
default_url = "tabungan:index"  # mengarahkan pada namespace saat pertama kali addons dibuka
```
