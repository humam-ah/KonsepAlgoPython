def a(angka):
  for baru in range(1,len(angka)):
    sisip = baru
    while angka[sisip] < angka[sisip-1] and sisip>0:
      angka[sisip],angka[sisip-1] = angka[sisip-1],angka[sisip]
      sisip = sisip -1
          
angka = []
for i in range(10):
  print('Data ke-',i+1,': ',sep='',end='')
  angka.append(int(input()))

print()
print('Data sebelum diurutkan: ',angka)
a(angka)
print('Data setelah diurutkan: ',angka)