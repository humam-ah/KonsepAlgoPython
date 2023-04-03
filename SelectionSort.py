def a(angka):
    for t in range(len(angka)-1,0,-1):
        m = 0
        for i in range(1,t+1):
            max = angka[m]
            if max < angka[i]:
                m = i
        angka[m],angka[t] = angka[t],angka[m]

angka = []
for i in range(10):
  print('Data ke-',i+1,': ',sep='',end='')
  angka.append(int(input()))

print()
print('Data sebelum diurutkan: ', angka)
a(angka)
print('Data setelah diurutkan: ', angka)                