#Pertemuan 10
Nama = ['Anny', 'Beni', 'Cici', 'Dona']
Nmat = [60,70,80,90]
Nstat = [75,65,75,95]
Nkom = [70,80,90,60]
print('=============================================================================================================================')
print('                                             DATA NILAI SISWA                                                                ')
print('=============================================================================================================================')
print('Nama' , 'N.Mat' , 'N.Stat' , 'N.Kom' , 'Rata-rata' , sep='\t')
print('=============================================================================================================================')
Mean = []
for i in range (0,len(Nama)) :
    Mean.append((Nmat[i] + Nstat[i] + Nkom[i])/3)
    print(Nama[i] , Nmat[i] , Nstat[i] , Nkom[i] , round(Mean[i],2) , sep='\t')
print('=============================================================================================================================')
p = 'y'
while p == 'y' :
    print('')
    print('Menu Mengubah Data' , '\n')
    print(' 1. Mengubah data')
    print(' 2. Menambah data')
    print(' 3. Menghapus data')
    print(' 4. Menranking data')
    print(' 5. Keluar')
    print('')
    Option = int(input('Pilih 1/2/3/4/5 : '))
    if Option == 1 :
        print('UBAH DATA' , '\n')
        print('Masukkan Data Baru' , '\n')
        Change = (int(input('Nomor yang ingin diubah : ')))
        for k in range (0,len(Nama)) :
            if k == Change - 1 :
                Nama[k] = str(input('Nama : '))
                Nmat[k] = int(input('Nilai Matematika : '))
                Nstat[k] = int(input('Nilai Statistika : '))
                Nkom[k] = int(input('Nilai Komputer : '))
    if Option == 2 :
        print('TAMBAH DATA' , '\n')
        print('Masukan Data Tambahan' , '\n')
        Nama.append(str(input('Nama : ')))
        Nmat.append(int(input('Nilai Matematika : ')))
        Nstat.append(int(input('Nilai Statistika : ')))
        Nkom.append(int(input('Nilai Komputer : ')))
    if Option == 3 :
        print('HAPUS DATA' , '\n')
        Delete = (int(input('Nomor yang ingin dihapus : ')))
        for k in range (0,len(Nama)) :
            if k == Delete - 1 :
                Nama.pop(k)
                Nmat.pop(k)
                Nstat.pop(k)
                Nkom.pop(k)
    if Option == 4 :
        print('RANKING DATA DATA')
        print('Menu Meranking Data' , '\n')
        print(' 1. Menurut Nilai Matematika')
        print(' 2. Menurut Nilai Statistika')
        print(' 3. Menurut Nilai Komputer')
        print(' 4. Menurut Rata-rata')
        Filter = int(input('Pilih 1/2/3/4/5 : '))
        if Filter == 1 :
            for i in range (0,len(Nama)-1) :
                for j in range (i+1,len(Nama)) :
                    if Nmat[i] < Nmat[j] :
                        a = Nmat[i]
                        b = Nama[i]
                        c = Nstat[i]
                        d = Nkom[i]
                        e = Mean[i]
                        Nmat[i] = Nmat[j]
                        Nama[i] = Nama [j]
                        Nstat[i] = Nstat[j]
                        Nkom[i] = Nkom[j]
                        Mean[i] = Mean[j]
                        Nmat[j] = a
                        Nama[j] = b
                        Nstat[j] = c
                        Nkom[j] = d
                        Mean[j] = e
        if Filter == 2 :
            for i in range (0,len(Nama)-1) :
                for j in range (i+1,len(Nama)) :
                    if Nstat[i] < Nstat[j] :
                        a = Nstat[i]
                        b = Nama[i]
                        c = Nmat[i]
                        d = Nkom[i]
                        e = Mean[i]
                        Nstat[i] = Nstat[j]
                        Nama[i] = Nama [j]
                        Nmat[i] = Nmat[j]
                        Nkom[i] = Nkom[j]
                        Mean[i] = Mean[j]
                        Nstat[j] = a
                        Nama[j] = b
                        Nmat[j] = c
                        Nkom[j] = d
                        Mean[j] = e
        if Filter == 3 :
            for i in range (0,len(Nama)-1) :
                for j in range (i+1,len(Nama)) :
                    if Nkom[i] < Nkom[j] :
                        a = Nstat[i]
                        b = Nama[i]
                        c = Nmat[i]
                        d = Nkom[i]
                        e = Mean[i]
                        Nstat[i] = Nstat[j]
                        Nama[i] = Nama [j]
                        Nmat[i] = Nmat[j]
                        Nkom[i] = Nkom[j]
                        Mean[i] = Mean[j]
                        Nstat[j] = a
                        Nama[j] = b
                        Nmat[j] = c
                        Nkom[j] = d
                        Mean[j] = e
        if Filter == 4 :
            for i in range (0,len(Nama)-1) :
                for j in range (i+1,len(Nama)) :
                    if Mean[i] < Mean[j] :
                        a = Nstat[i]
                        b = Nama[i]
                        c = Nmat[i]
                        d = Nkom[i]
                        e = Mean[i]
                        Nstat[i] = Nstat[j]
                        Nama[i] = Nama [j]
                        Nmat[i] = Nmat[j]
                        Nkom[i] = Nkom[j]
                        Mean[i] = Mean[j]
                        Nstat[j] = a
                        Nama[j] = b
                        Nmat[j] = c
                        Nkom[j] = d
                        Mean[j] = e
    print('')
    print('=============================================================================================================================')
    print('                                             DATA NILAI SISWA                                                                ')
    print('=============================================================================================================================')
    print('Nama' , 'N.Mat' , 'N.Stat' , 'N.Kom' , 'Rata-rata' , sep='\t')
    print('=============================================================================================================================')
    Mean = []
    for i in range (0,len(Nama)) :
        Mean.append((Nmat[i] + Nstat[i] + Nkom[i])/3)
        print(Nama[i] , Nmat[i] , Nstat[i] , Nkom[i] , round(Mean[i],2) , sep='\t')
    print('=============================================================================================================================')
    p = input('Apakah ingin menubah data kembali ? y/t : ')
