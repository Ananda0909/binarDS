def tambah(angka_1, angka_2):
    """Funfsi menambah 2 angka """
    return angka_1 + angka_2

print("masukkan angka 1: ")
angka_1 = float(input())
print("masukkan angka 2: ")
angka_2 = float(input())

hasil = tambah(angka_1, angka_2)
print(f"Hasilnya: {hasil}")