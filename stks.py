import numpy as np
#1. suhu c ke f
suhu_c = np.array([22, 19, 17, 20, 22, 23, 21, 19, 22, 24])
suhu_f = (suhu_c * 9/5) + 32

print("suhu celcius: ", suhu_c)
print("suhu fahrenheit: ", suhu_f)

#2. sortir data nilai
nilai = np.array([80, 78, 68, 99, 87, 79, 69, 87, 83, 75,
                  82, 92, 82, 74, 94, 96, 95, 98, 79, 80,
                  91, 88, 93, 97, 92, 80, 65, 75, 99, 73])
nilai_u = np.sort(nilai)[::-1] #reverse_sort
print("nilai ujian siswa sebelum diurut: ", nilai)
print("nilai ujian siswa setelah diurut: ", nilai_u)
print("nilai ujian 5 besar: ", nilai_u[0:5])

#3. keuntungan penjualan
untung = np.array([200000, 230000, 210000, 180000, 130000, 190000, 240000,
                   290000, 240000, 250000, 190000, 190000, 230000, 300000])

rata2 = np.mean(untung)
untung_urut = np.sort(untung)
max_untung = untung_urut[-1:]#max
min_untung = untung_urut[:1]#min
max_index = np.where(untung == max_untung)[0][0] + 1
min_index = np.where(untung == min_untung)[0][0] + 1

print(f"rata: rp{rata2}")
print(f"keuntungan tertinggi: rp{max_untung} (hari ke-{max_index})")
print(f"keuntungan terendah: rp{min_untung} (hari ke-{min_index})")
