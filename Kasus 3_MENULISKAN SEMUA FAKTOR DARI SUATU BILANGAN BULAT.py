print('MENULISKAN SEMUA FAKTOR DARI SUATU BILANGAN BULAT')
print('')
print('Dibuat oleh : Gabriel Olivia Yvonne Manurung')
print('NIM: 1305621023')
print('')
n = int(input('Masukan bilangan bulat n : '))
print('')
print('Faktor dari',n,'adalah:')
faktor_dari_n = []
for i in range(1, n+1):
    if n% i== 0:
        faktor_dari_n.append(i)
        print(i,end=',')
