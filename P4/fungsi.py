import os

def create_directory(nama_folder):
    # Membuat folder jika belum ada
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)
        print(f"Direktori '{nama_folder}' berhasil dibuat.")
    else:
        print(f"Direktori '{nama_folder}' sudah ada.")