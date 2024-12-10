
# RETURN VS PRINT

#PRINT
print('USING PRINT')
def hitung_luas_segitiga(alas,tinggi):
    luas = (alas*tinggi)/2
    print('Luas segitiga adalah: ',luas)

hitung_luas_segitiga(5,7)

print(50*'=')

#RETURN
print('USING RETURN')
def hitung_luas_segitiga(alas,tinggi):
    luas = (alas*tinggi)/2
    return luas

var1 = hitung_luas_segitiga(5,7)
print('Luas segitiga adalah: ',var1)
