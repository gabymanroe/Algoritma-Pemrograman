#MATRIKS ORDO 2x2
#-----------------------PENJUMLAHAN----------------------
print('Penjumlahan Matriks Ordo 2x2')
print()

matriks1=[
    [2,5],
    [-1,7]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],sep='\n')
print()

matriks2=[
    [1,-9],
    [8,4]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],sep='\n')
print()

print('Matriks 1 + Matriks 2 = ')
for i in range (0,len(matriks1)):
    for j in range(0,len(matriks1[0])):
        hasil=matriks1[i][j]+matriks2[i][j]
        print(hasil, end='  ')
    print()
    
#-----------------------PENGURANGAN----------------------
print()
print(50*'=')
print('Pengurangan Matriks Ordo 2x2')
print()

matriks1=[
    [2,5],
    [-1,7]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],sep='\n')
print()

matriks2=[
    [1,-9],
    [8,4]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],sep='\n')
print()

print('Matriks 1 - Matriks 2 = ')
for i in range (0,len(matriks1)):
    for j in range(0,len(matriks1[0])):
        hasil=matriks1[i][j]-matriks2[i][j]
        print(hasil, end='  ')
    print()

#-----------------------PERKALIAN----------------------
print()
print(50*'=')
print('Perkalian Matriks Ordo 2x2')
print()

matriks1=[
    [2,5],
    [1,7]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],sep='\n')
print()

matriks2=[
    [-1,-9],
    [8,4]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],sep='\n')
print()

matriks3=[]

print('Matriks 1 x Matriks 2 = ')

for i in range (0,len(matriks1)):
    baris=[]
    for j in range(0,len(matriks1[0])):
        hasil=0
        for k in range(0,len(matriks1)):
            hasil=hasil+(matriks1[i][k]*matriks2[k][j])
        baris.append(hasil)
    matriks3.append(baris)

for i in range(0,len(matriks3)):
    for j in range(0,len(matriks3[0])):
        print(matriks3[i][j],end='  ')
    print()
