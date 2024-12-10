print(50*'=')
print('Data Nilai Mahasiswa')
print(50*'=')

n=int(input('Banyak Mahasiswa='))
print()
namamhs=[]
nmhs=[]
nhuruf=[]
for i in range(n):
    namamhs.append(str(input('Nama Mahasiswa=')))
    nmhs.append(round(int(input('Nilai Mahasiswa='))))
print()

print()
print(50*'-')
print('Nama Mahasiswa','Nilai Mahasiswa','Nilai Huruf', sep='\t')
for i in range (n):
    if 0 <= nmhs[i] <= 45:
        huruf = 'E'
        keterangan = 'Belum Lulus'
    elif 46 <= nmhs[i] <= 50:
        huruf = 'D'
        keterangan = 'Belum Lulus'
    elif 51 <= nmhs[i] <= 55:
        huruf = 'C-'
        keterangan = 'Belum Lulus'
    elif 56 <= nmhs[i] <= 60:
        huruf = 'C'
        keterangan = 'Lulus'
    elif 61 <= nmhs[i] <= 65:
        huruf = 'C+'
        keterangan = 'Lulus'
    elif 66 <= nmhs[i] <= 70:
        huruf = 'B-'
        keterangan = 'Lulus'
    elif 71 <= nmhs[i] <= 75:
        huruf = 'B'
        keterangan = 'Lulus'
    elif 76 <= nmhs[i] <= 80:
        huruf = 'B+'
        keterangan = 'Lulus'
    elif 81 <= nmhs[i] <= 85:
        huruf = 'A-'
        keterangan = 'Lulus'
    elif 46 <= nmhs[i] <= 50:
        huruf = 'A'
        keterangan = 'Lulus'
    else:
        huruf = '-'
    h.append(str(huruf))
    print(namamhs[i],nmhs[i],nhuruf[i],keterangan[i],sep='\t')
print(50*'-')
