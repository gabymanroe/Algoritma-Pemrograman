#CARA 1
print('CARA 1')
def faktorial_dari(n):
    if n==1:
        return 1
    else:
        return n*faktorial_dari(n-1)

print(faktorial_dari(5))

print(50*'=')

#CARA 2
print('CARA 2')
def faktorial(n):
    hasil_faktorial=1
    for i in range (2,n+1):
        hasil_faktorial=hasil_faktorial*i
    return hasil_faktorial

for j in range(1,11):
    print(str(j)+'!= ',faktorial(j))
