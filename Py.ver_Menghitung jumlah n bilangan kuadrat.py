print('Menghitung jumlah n bilangan kuadrat')
print('Sn = 1 + 4 + ... + n^2')
n = int(input('n = '))
i=1
Sn=0
print('Sn = ',end='')
for i in range (i,n):
    print((i**2),end='+')
    Sn=Sn+i**2
    i=i+1
Sn=Sn+n**2
print(n**2,'=',Sn)
