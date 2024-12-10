
print('Membuat Tabel Distribusi Frekuensi')
nilai=[60,65,70,75,80,75,70,70,80,80,45,50,60,90,60,70,80,90,60,75,65,45,55,85,75,45,65,95,80,55,65,75,85,50,60,70,80,80,70,50]

print('Data nilai: ')
print(nilai[0:10],nilai[10:20],nilai[20:30],nilai[30:40],sep='\n')
print()
print('TABEL DSTRIBUSI FREKUENSI')
print(30*'-')
print('Interval Kelas', ' |  Frekuensi', sep='\t')
print(30*'-')
IK = [41,51,61,71,81,91]
IK2 = [50,60,70,80,90,100]
f=[0,0,0,0,0,0]
for j in range(0,6):
    for i in range(0,len(nilai)):
        if IK[j]<=nilai[i]<=IK2[j]:
            f[j]=f[j]+1
    print('   ',IK[j],'-',IK2[j],'\t','|','   ',f[j])
print(30*'-')
print('Banyak Data: ',len(nilai),sep='\t')

#Mencari Modus
fkm=0
b=0
d1=0
d2=0
c=0

for k in range (0,len(f)):
    if f[k]>fkm:
        b=IK[k]-0.5
        c=IK2[k]-IK[k]+1
        fkm=f[k]
        if fkm==f[0]:
            d1=fkm-0
            d2=fkm-f[k+1]
        elif fkm==f[len(f)-1]:
            d1=fkm-f[k-1]
            d2=fkm-0
        else:
            d1=fkm-f[k-1]
            d2=fkm-f[k+1]
for k in range(0,len(f)):
    if f[k]==fkm:
        print('\n''Kelas Modus = ',IK[k],'-',IK2[k],
              '\n''Frekuensi Kelas Modus = ',fkm,
              '\n''d1 = ',d1,
              '\n''d2 = ',d2,
              '\n''Panjang kelas (c) = ',c,
              '\n''Tepi Bawah Kelas Modus = ',b)
Mo = b + (d1/(d1+d2))*c
print('\n''Modus data berkelompok = ',Mo)
