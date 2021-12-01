jumlah = 0
i = 0
print("masukkan angka: ")
angka = int(input())
while angka != 9999:
    i = i + 1
    jumlah = jumlah + angka
    print("masukkan angka: ")
    angka = int(input())
ratarata = float(jumlah) / i
print("Rata ratanya adalah: " + str(ratarata))
