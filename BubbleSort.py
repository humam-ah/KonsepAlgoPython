def a(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                urut = x[j]
                x[j]=x[j+1]
                x[j+1]=urut

angka = []
for i in range(10):
  print('Data ke-',i+1,': ',sep='',end='')
  angka.append(int(input()))

print()
print('Data sebelum diurutkan: ', angka)
a(angka)
print('Data setelah diurutkan: ', angka)