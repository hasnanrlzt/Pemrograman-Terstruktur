x = int(input('Banyak data yang ingin dimasukkan : '))
y = 0
data = []
print('==============================')
for y in range (x):
    print('Nama Mahasiswa  : ')
    d = input()
    z = len(d)
    e = d+' ('+ str(z)+ ' karakter)'
    data.append(e)
data.sort()
print('==============================')
for i in data:
    print(i)

