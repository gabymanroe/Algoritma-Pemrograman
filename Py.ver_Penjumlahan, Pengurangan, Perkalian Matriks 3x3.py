#MATRIKS ORDO 3x3
#-----------------------PENJUMLAHAN----------------------
print('Penjumlahan Matriks Ordo 3x3')
print()

matriks1=[
    [2,5,0],
    [-1,7,1],
    [0,0,3]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],matriks1[2],sep='\n')
print()

matriks2=[
    [1,-9,-8],
    [8,4,4],
    [1,1,0]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],matriks2[2],sep='\n')
print()

print('Matriks 1 + Matriks 2 = ')
for i in range (0,len(matriks1)):
    for j in range(0,len(matriks1[0])):
        hasil=matriks1[i][j]+matriks2[i][j]
        print(hasil, end='\t')
    print()
    
#-----------------------PENGURANGAN----------------------
print()
print(50*'=')
print('Pengurangan Matriks Ordo 3x3')
print()

matriks1=[
    [2,5,0],
    [-1,7,1],
    [0,0,3]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],matriks1[2],sep='\n')
print()

matriks2=[
    [1,-9,-8],
    [8,4,4],
    [1,1,0]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],matriks2[2],sep='\n')
print()

print('Matriks 1 - Matriks 2 = ')
for i in range (0,len(matriks1)):
    for j in range(0,len(matriks1[0])):
        hasil=matriks1[i][j]-matriks2[i][j]
        print(hasil,end='\t')
    print()

#-----------------------PERKALIAN----------------------
print()
print(50*'=')
print('Perkalian Matriks Ordo 3x3')
print()

matriks1=[
    [2,5,0],
    [-1,7,1],
    [0,0,3]
]
print('Matriks 1: ')
print(matriks1[0],matriks1[1],matriks1[2],sep='\n')
print()

matriks2=[
    [1,-9,-8],
    [8,4,4],
    [1,1,0]
]
print('Matriks 2: ')
print(matriks2[0],matriks2[1],matriks2[2],sep='\n')
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
        print(matriks3[i][j],end='\t')
    print()
