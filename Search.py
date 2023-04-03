print('Input 10 angka (dipisah dengan enter): ');
 
# simpan setiap angka yang diinput ke dalam list
x = []
for i in range(10):
  print('Angka ke-',i+1,': ',sep='',end='')
  x.append(int(input()))
 
print()
 
angka = int(input('Input angka yang akan dicari: '))
  
# proses pencarian element list
for i in range(10):
  if(x[i]==angka):
    print('Angka ditemukan pada urutan ke',i+1)
    break
 
if(i+1 == 10):
  print('Angka tidak ditemukan')