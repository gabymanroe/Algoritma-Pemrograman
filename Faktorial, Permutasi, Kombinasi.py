print()
print(72*'=')

def Faktorial (n):
        Hasil = 1
        for i in range (1,n+1):
            Hasil = Hasil*i
        return Hasil
        
p='y'
while p == 'y' :
    print()
    print('Menu :')
    print('1. Menentukan hasil fungsi faktorial')
    print('2. Menentukan hasil Permutasi')
    print('3. Menentukan hasil Kombinasi')
    print()
    pilih = int(input('pilih 1/2/3: '))
    print()
    print(50*'=')

    if pilih == 1 :
        print('\t\tMenentukan hasil fungsi faktorial')
        print()
        print('Fungsi faktorial didefinisikan dengan n!')
        def Faktorial (n):
            Hasil = 1
            for i in range (1,n+1):
                Hasil = Hasil*i
            return Hasil
        n=(int(input('Masukkan nilai n = ')))
        print()
        if n>=0 :
            print('Maka hasil dari',n,'!',' = ',Faktorial(n))
            print()

        else:
            print('Tidak terdefinisi')

    if pilih == 2:
        print('Menentukan Hasil Permutasi')
        print()
        def Permutasi(m,r):
            Hasil = Faktorial(m)/Faktorial(m-r)
            return Hasil
        m=(int(input('Masukkan nilai m = ')))
        r=(int(input('Masukkan nilai r = ')))

        if m>=0:
            if r>=0:
                if m>r:
                    print('Permutasi dari ',m,'dan',r,'adalah ', Permutasi(m,r))
                else:
                    print('Nilai m lebih besar dari r, sehingga permutasi tidak terdefinisi')
            else:
                print('Tidak terdefinisi')
        else:
            print('Tidak terdefinisi')

    if pilih == 3:
        print('Menentukan Hasil Kombinasi')
        print()
        def Kombinasi(m,r):
            Hasil = Faktorial(m)/(Faktorial(r)*Faktorial(m-r))
            return Hasil
        m=(int(input('Masukkan nilai m = ')))
        r=(int(input('Masukkan nilai r = ')))
        if m>=0:
            if r>=0:
                if m>r:
                    print('Kombinasi dari ',m,'dan',r,'adalah ', Kombinasi(m,r))
                else:
                    print('Nilai m lebih besar dari r, sehingga permutasi tidak terdefinisi')
            else:
                print('Tidak terdefinisi')
        else:
            print('Tidak terdefinisi')

        
    print()
    print(72*'-')
    p=input('Mencoba lagi y/t : ')
    

print()
print('Program Berhenti')
print(72*'=')

