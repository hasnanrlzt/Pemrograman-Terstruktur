#Nomor 1
print('#Nomor 1')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#Nomor 2
print('#Nomor 2')
a[3] = 10
print(a)
b[-1] = 8
print(b)

#Nomor 3
print('#Nomor 3')
a[-1] = 10
print(a)
b[-1] = 8
print(b)

#Nomor 4
print('#Nomor 4')
a.sort()
print(a)
b.sort()
print(b)

#Nomor 5
print('#Nomor 5')
c = a[0:7]
d = b[2:9]
print(c)
print(d)

#Nomor 6
print('#Nomor 6')
e=[]
i=0
for i in range (len(d)):
    indeks=c[i]+d[i]
    e+= [indeks]
e.append(c[-1])
print(e)

#Nomor 7
print('#Nomor 7')
myTuple = tuple(e)
print(myTuple)

#Nomor 8
print('#Nomor 8')
print('Nilai Minimal =', min(e))
print('Nilai Maksimal =', max(e))
print('Jumlah seluruh elemen dari e adalah ', sum(e))

#Nomor 9
print('#Nomor 9')
myString= "python adalah bahasa pemrograman yang menyenangkan"

#Nomor 10
print('#Nomor 10')
huruf = set(myString)
huruf.remove(' ')
print("Kalimat terususn atas hururf : ", huruf)

#Nomor 11
print('#Nomor 11')
#Mengubah ke dalam bentuk list
letter = list(huruf)
print(letter)
#Mengurutkan secara alfabet
letter.sort()
print(letter)

















