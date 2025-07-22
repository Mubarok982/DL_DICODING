import nbformat

# Ganti dengan nama file kamu
file_path = "Latihan_Text_Prepocessing.ipynb"

# Buka notebook
nb = nbformat.read(file_path, as_version=4)

# Hapus metadata.widgets jika ada
if "widgets" in nb["metadata"]:
    print("Menghapus metadata.widgets...")
    del nb["metadata"]["widgets"]
else:
    print("metadata.widgets tidak ditemukan, file aman.")

# Tulis ulang file
nbformat.write(nb, file_path)
print("✅ File berhasil diperbaiki dan disimpan.")
