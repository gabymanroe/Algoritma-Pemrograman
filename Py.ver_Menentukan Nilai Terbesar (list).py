print("Menentukan Bilangan Terbesar")
print(30*"-")

data =[50,95,65,74,45,60,78,95,80,95]
nama =["Amir", "Budi", "Cici", "Dani", "Erni", "Fira", "Ghina", "Hasna", "Indah", "Karina"]

db=data[0]
jk=nama[0]

print("Data yang dimasukkan: ","\n")
print("Nomor", "Nama","Nilai", sep="\t")

for i in range(0,10):
    print(i+1,nama[i],data[i],sep="\t")
    if db<data[i]:
        db=data[i]
        jk=nama[i]

print("")
print("Data terbesar = ",db)
print("Juara Kelas = ",jk)
for i in range (0,10):
    if data[i]==db:
        if i<9:
            print(nama[i], end = " , ")
        else:
             print(nama[i])
