#program hitung tarif rental

tarif1 = 200000
tarif2 = 10000
JamMulai = 6
MenitMulai = 0
JamSelesai = 23
MenitSelesai = 50

JamSewa = JamSelesai - JamMulai
MenitSewa = MenitSelesai - MenitMulai

LamaSewa = int(JamSewa + MenitSewa / 60)

TotalBiaya = int(tarif1 + tarif2 * (LamaSewa - 12))

print("Total tarif rental mobil yang harus dibayarkan adalah ",TotalBiaya)
