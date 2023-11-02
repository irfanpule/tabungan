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
