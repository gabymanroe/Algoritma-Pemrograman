#Pertemuan 11: Input Matriks
print('=============================================================================================================================')
print('                                         MENGINPUT MATRIKS MATRIKS                                                           ')
print('=============================================================================================================================')
y = int(input('Masukan banyak matriks = '))
n = 0
A = []
R = []
C = []
while y > n :
    A.append([])
    print('=============================================================================================================================')
    print('MATRIKS KE ' , n+1)
    R.append(int(input('Ukuran baris matriks = ')))
    C.append(int(input('Ukuran kolom matriks = ')))
    Matriks = []
    print('=============================================================================================================================')
    print('Masukan elemen matriks A :')
    for i in range (0,R[n]) :
        Matriks.append([]*R[n])
        for j in range (0,C[n]) :
            print('Masukan elemen a' + str(i+1) + str(j+1) , end=' ')
            Matriks[i].append(int(input(' = ')))
    A[n] = Matriks
    print('=============================================================================================================================')
    print('MATRIKS A' + str(n+1) +' :')
    for i in range (0,R[n]) :
        for j in range (0,C[n]) :
            print(A[n][i][j], end='\t')
        print()
    n = n+1
    print('=============================================================================================================================')
if R[0] == R[1] :
    if C[0] == C[1] :
        print('MATRIKS B = A1 + B2 :')
        for i in range (0,R[0]) :
            for j in range (0,C[0]) :
                print(A[0][i][j] + A[1][i][j], end='\t')
            print()
        print('=============================================================================================================================')
    else :
        print('Ukuran matriks tidak sama')
else :
    print('Ukuran matriks tidak sama')
