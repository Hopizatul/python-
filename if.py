nama = input("masukkan nama: ")
usia = int(input("masukkan usia: "))
berat_badan = float(input("masukkan berat badan: "))
tek_darah = float (input("masukkan tekanan darah: "))

layak = True
if usia < 17 or usia > 60:
    layak = False
if berat_badan < 45:
    layak = False
if tek_darah < 100 or tek_darah > 160:
    layak = False

if layak:
    print(f"{nama} layak untuk donor darah")
else:
    print(f"{nama} tidak layak donor darah")