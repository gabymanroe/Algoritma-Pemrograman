print('')
print('MENENTUKAN DATA KE-i')
nilai=[8,2,9,4,7,5,8,6]
print('')
print('List Nilai: ')
for i in range (8):
    print('Urutan nilai ke-(',i,')=',nilai[i])
nb=max(nilai)
nk=min(nilai)
print('\n''Nilai terbesar adalah ',nb,
      '\n''Nilai terkecil adalah ',nk)
print('')

print(50*'=')
#ANOTHER WAY
print('')
print('MENENTUKAN DATA KE-i')
nilai=[8,2,9,4,7,5,8,6]
print('')
print('List Nilai: ')
nt=nilai[0]
for i in range (0,len(nilai)):
    print('Urutan nilai ke-(',i,')=',nilai[i])
    if nb<nilai[i]:
        nb=nilai[i]
    if nk>nilai[i]:
        nk=nilai[i]
print('\n''Nilai terbesar adalah ',nb,
      '\n''Nilai terkecil adalah ',nk)
