def karakter_ganjil(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 1:
            result += input_string[i]
    return result

# Input dari pengguna
input_user = input("Masukkan sebuah string: ")

# Memanggil fungsi dan mencetak hasil
hasil = karakter_ganjil(input_user)
print("Karakter dengan indeks ganjil:", hasil)


