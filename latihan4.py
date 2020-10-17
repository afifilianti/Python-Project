#program hitung waktu

JarakPertama = 125
KecepatanPertama = 62

JarakKedua = 256
KecepatanKedua = 70

WaktuBerangkat = 06.00
WaktuIstirahat = 0.45

WaktuAB = round(JarakPertama / KecepatanPertama)
WaktuBC = round(JarakKedua / KecepatanKedua)

WaktuSampai = WaktuBerangkat + WaktuAB + WaktuBC + WaktuIstirahat

print("Waktu sampai Pak Amir di kota C pukul :", WaktuSampai)
