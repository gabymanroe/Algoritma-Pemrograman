a=int(input('Masukkan nilai a: '))
b=int(input('Masukkan nilai b: '))

def FPB(a,b):
    if a>b:
        nk=b
    if b>a:
        nk=a
    if a==b:
        nk=a=b
    for i in range(1,nk+1):
        if(a%i==0)and(b%i==0):
            fpb=i
    return fpb

print('FPB dari',a,'dan',b,'adalah',FPB(a,b))
