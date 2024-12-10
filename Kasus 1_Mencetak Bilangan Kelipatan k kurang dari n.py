print('='*50)
print('Mencetak Bilangan Kelipatan k kurang dari n')
print('='*50)
print('Dibuat oleh : Gabriel Olivia Yvonne Manurung')
print('')

n = int(input('Batas atas keliapatan angka =  '))
k = int(input('Masukkan angka yang dicari kelipatannya = '))
print('')

hasil1=k
hasil2=[]
for i in range(k):
    x=1
    while hasil1<n-k:
        hasil1=k*x
        x=x+1
        hasil2.append(int(hasil1))
print('Bilangan kelipatan',k,'kurang dari',n,'adalah:')
print(hasil2)
