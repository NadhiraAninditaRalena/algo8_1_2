def hitung_jumlah_range(start, end):
    total = sum(range(start, end + 1))
    return total

# Input dari pengguna
angka_awal = int(input("Masukkan angka awal: "))
angka_kedua = int(input("Masukkan angka kedua: "))

# Memanggil fungsi dan mencetak hasil
hasil = hitung_jumlah_range(angka_awal, angka_kedua)
print(f"Jumlah range dari {angka_awal} dan {angka_kedua} adalah: {hasil}")

