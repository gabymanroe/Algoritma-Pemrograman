print("Menghitung luas segitiga sembarang")

a = float(input("Masukkan panjang sisi a = "))
b = float(input("Masukkan panjang sisi b = "))
c = float(input("Masukkan panjang sisi c = "))

if a+b>c and a+c>b and b+c>a:
    s = (a+b+c)/2
    L = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Maka luas segitiga sembarang tersebut adalah", L)
else:
    print("a,b,dan c bukanlah sisi-sisi dari sebuah segitiga")
