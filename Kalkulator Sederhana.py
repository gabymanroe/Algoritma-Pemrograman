#Membuat Kalkulator sederhana dengan Fungsi/Subrutin/Subprogram
print("Kalkulator Sederhana")
print()

#Menu Operasi
def masukkan():
    a = int(input("Masukkan Bilangan pertama: "))
    b = int(input("Masukkan Bilangan kedua: "))
    return Menu(a, b)

def Menu(e, f):
    print("1. Penjumlahan","\n",
            "2. Pengurangan","\n",
            "3. Perkalian","\n",
            "4. Pembagian")
    print("Operasi apa yang akan anda gunakan?")
    a = int(input("Jawab: "))
    if a == 1:
        print("Hasilnya: ", jumlah(e, f))
        return pertulang()
    elif a == 2:
        print("Hasilnya: ", kurang(e, f))
        return pertulang()
    elif a == 3:
        print("Hasilnya: ", kali(e, f))
        return pertulang()
    elif a == 4:
        print("Hasilnya: ", bagi(e, f))
        return pertulang()
    else:
        print("Jangan Tulis macem-macem angka aja sesuai menu")
        return Menu(e, f)

def pertulang():
    print("Apakah anda ingin menggunakan program lagi? (Ya/Tidak)")
    P = str(input("Jawab: "))
    if P == "Ya":
        return masukkan()
    elif P == "Tidak":
        o = "Terima Kasih telah menggunakan Program ini"
        return o
    else:
        print("Jangan Tulis macem-macem cukup Ya/Tidak")
        return pertulang()

def jumlah(s, t):
    A = s + t
    return A
def kurang(s, t):
    B = s - t
    return B
def kali(s, t):
    C = s*t
    return C
def bagi(s, t):
    D = s/t
    return D

print(masukkan())
