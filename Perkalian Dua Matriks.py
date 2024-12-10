#Perkalian Dua Matriks
ulang='y'
while ulang=='y':
    print ('                                                                                          -         Perkalian Dua Matriks          -                                                                                         ')
    n=int(input('∴ Banyak Matriks (n) = '))
    p=0
    A=[]
    baris=[]
    kolom=[]
    print()
    while p<n:
        A.append([])
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('∴ Matriks Ke -',p+1)
        baris.append(int(input('    - Banyak baris : ')))
        kolom.append(int(input('    - Banyak kolom : ')))
        print()
        print('    Input Elemen Matriks Ke -',p+1)
        matriks=[]
        for i in range (0, baris[p]):
            matriks.append([])
            for j in range (0, kolom[p]):
                print('    ✏ a'+str(i+1)+str(j+1), end=' ')
                matriks[i].append(int(input(' = ')))
        A[p]=matriks
        print()
        print('∴ Matriks A'+str(p+1),':')
        for i in range (0,baris[p]):
            print('   [',end='')
            for j in range (0,kolom[p]):
                print('      ',A[p][i][j], end= '      ')
            print(']')
        print()
        p=p+1
    if kolom[0]==baris[1]:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('                                                                          PERKALIAN MATRIKS A1 (baris × t) DAN A2 (t × kolom)                                                                          ')
        print('                                                                                PERKALIAN MATRIKS A1 (',baris[0],'×',kolom[0],') DAN A2 (',baris[1],'×',kolom[1],')')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Misalkan Matriks A1=A dan Matriks A2=B ')
        print('∴ Maka, matriks C = A × B')
        for i in range (0,baris[0]):
            print('   [',end='')
            for j in range (0,kolom[1]):
                print('      ', end='')
                for k in range (0,kolom[0]):
                    print(end='')
                    if k<(kolom[0]-1):
                        print('(a'+str(i+1)+str(k+1),'× b'+str(k+1)+str(j+1),') + ',end='')
                    else:
                        print('(a'+str(i+1)+str(k+1),'× b'+str(k+1)+str(j+1),')',end='      ')
            print(']')
        print()
        for i in range (0,baris[0]):
            print('   [',end='')
            for j in range (0,kolom[1]):
                print('      ', end='')
                for k in range (0,kolom[0]):
                    print(end='')
                    if k<(kolom[0]-1):
                        print('(',A[0][i][k],'×',A[1][k][j],') + ',end='')
                    else:
                        print('(',A[0][i][k],'×',A[1][k][j],')',end='      ')
            print(']')
        print()
        for i in range (0,baris[0]):
            print('   [',end='')
            for j in range (0,kolom[1]):
                print('      ', end='')
                for k in range (0,kolom[0]):
                    print(end='')
                    if k<(kolom[0]-1):
                        print('(',A[0][i][k]*A[1][k][j],') + ',end='')
                    else:
                        print('(',A[0][i][k]*A[1][k][j],')',end='      ')
            print(']')
        print()
        C = []
        print('∴ Matriks C:')
        for i in range (0, baris[0]):
            print('   [',end='')
            C.append([])
            for j in range (0, kolom[1]):
                z = 0
                for k in range (0,kolom[0]):
                    z = z + (A[0][i][k]*A[1][k][j])
                C[i].append(z)
                print ('    ',C[i][j], end = '      ')
            print(']')
        print()
    else:
        print('                                                  ❌TIDAK BISA DIKALIKAN❌                                                       ')
        print('                                                           Kolom A1 ≠ Baris A2                                                                  ')
        print('                                                                       ', kolom[0], '≠', baris[1],'\n')
        print('❗ Ingat syarat perkalian matriks: Banyak kolom matriks pertama = Banyak baris matriks kedua ❗')
    print()
    ulang=input('Mencoba lagi (y/t): ')
    print()
    print('=================================================================================================================','\n')
print('----------------------------------------------------------------         PROGRAM PERKALIAN MATRIKS BERHENTI         ----------------------------------------------------------------','\n')

