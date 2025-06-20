import random

bil = random.randint (1, 100) # menghasilkan bilangan acak pada renteng 1 s.d 100
tebakan_benar = False
tebakan_maks = 7
jmlh_tebakan = 0

print("komputer telah memilih bilangan secara acak")
print("silahkan tebak angka tersebut")

while not tebakan_benar and jmlh_tebakan < tebakan_maks:
    jmlh_tebakan = jmlh_tebakan +1
    print(f"ini adalah tebakan ke- {jmlh_tebakan} anda ")
    tebakan = int(input("masukkan tebakan anda: "))
    if bil == tebakan:
        tebakan_benar = True
    elif bil > tebakan:
        print("tebakan anda kekecilan")
    else:
        print("tebakan anda kebesaran")

if tebakan_benar:
    print(f"selamat tebakan anda benar")
else:
    print(f"tebakan anda salah, bilangan yang benar {bil}")