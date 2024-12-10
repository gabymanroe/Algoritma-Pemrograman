print('PROGRAM MENENTUKAN NILAI HURUF DARI SUATU NILAI ANGKA')
print('')
print('Dibuat Oleh : Gabriel Olivia Yvonne Manurung','\n')

namamurid=['Amir','Budi','Cici','Deni','Enny','Fahmi']
nilaimurid=[50,65,70,75,56,90]
Nilai_Huruf = []
nilaiA = 0
nilaiB = 0
nilaiC = 0
nilaiD = 0
nilaiE = 0
nilai=0
for i in range(len(nilaimurid)):
    if 0 <= nilaimurid[i]<=50:
        j = 'E'
        nilaiE=nilaiE+1
    if 50< nilaimurid[i]<60:
        j = 'D'
        nilaiD=nilaiD+1
    if 60 <= nilaimurid[i]<75:
        j = 'C'
        nilaiC=nilaiC+1
    if 75<= nilaimurid[i]<85:
        j = 'B'
        nilaiB=nilaiB+1
    if 85<= nilaimurid[i]<=100:
        j = 'A'
        nilaiA=nilaiA+1
    Nilai_Huruf.append(str(j))
print('Nama: ',namamurid)
print('Nilai: ',nilaimurid)

print(40*'-')
print('Nama', ' |   Nilai', ' | N.Huruf',sep='\t')
print(40*'-')
for m in range(0,len(namamurid)):
    print(namamurid[m],'\t'' |   ',nilaimurid[m],'\t'' |   ',Nilai_Huruf[m])
print(40*'-')
