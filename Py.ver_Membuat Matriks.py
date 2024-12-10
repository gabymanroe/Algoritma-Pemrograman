
#M E M B U A T    M A T R I K S

b=int(input('Masukkan banyaknya baris pada matriks = '))
k=int(input('Masukkan banyaknya kolom pada matriks = '))

matriks1=[]
print('')
print('Matriks A')
for i in range(b):
    x=[]
    for j in range(k):
        j=int(input('Elemen matriks a'+str(i+1)+''+str(j+1)+': '))
        x.append(j)
    print()
    matriks1.append(x)
#print matriks
for i in range(b):
    for j in range(k):
        print(matriks1[i][j],end='  ')
    print()
