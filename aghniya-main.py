# Volume Tabung
r = float(input("Masukkan jari jari: "))
t = float(input("Masukkan tinggi: ")) 

def volTabung(r, t):
    vol =  3.14 * (r*r) * t
    return vol

print(f"Volume tabung tersebut : ", volTabung(r, t), "cm3")



# Nilai Total & Rata rata
def ratarata(*angka):
    hasil = sum(angka)
    rata2 = hasil / len(angka)
    return hasil, rata2

angka = input("Masukkan angka dipisahkan dengan spasi: ")

angka_list = [float(i) for i in angka.split()]

total, rata = ratarata(*angka_list)

print("Jumlah semua angka:", total)
print("Rata-rata:", rata)