# Clash of Clans API Client

Sebuah script sederhana untuk memanggil API **Clash of Clans** menggunakan Python. Script ini dapat:

- Mengambil informasi pemain berdasarkan **Player Tag**
- Mencari klan berdasarkan **Nama Klan**
- Menyimpan respons dalam format **JSON**

## Persiapan

Pastikan Anda memiliki:

- Python 3.x
- Library `requests` (`pip install requests`)
- **API Token** dari [Clash of Clans Developer Portal](https://developer.clashofclans.com/)

## Cara Penggunaan

1.  Clone repository:

    ```
    git clone https://github.com/adrianoposumah/ClashOfClansAPIRequest.git
    cd ClashOfClansAPIRequest
    ```

2.  Instal dependensi:

    ```
    Copy code
    pip install -r requirements.txt
    ```

3.  Jalankan script:

        ```
        python ClashOfClansAPIRequest.py

        ```

    > Pilih opsi:
    > 1: Ambil informasi pemain
    > 2: Cari klan
    > Masukkan Player Tag atau Nama Klan sesuai pilihan Anda.

Hasil
Setiap respons akan disimpan dalam file JSON:

Data pemain: player*<PlayerTag>.json
Data klan: clan*<NamaKlan>.json
markdown
Copy code

### Penjelasan Singkat:

1. **Persiapan**: Langkah untuk mempersiapkan Python dan library yang dibutuhkan.
2. **Cara Penggunaan**: Langkah-langkah untuk menjalankan script dan menambahkan API token.
3. **Hasil**: Menjelaskan bahwa hasil dari API akan disimpan dalam file JSON.
