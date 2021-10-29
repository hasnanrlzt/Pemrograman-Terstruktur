#Nomor 5
print('===========================================')
print('#Nomor 5a')
from operation import *

b = jumlah(2, -4)
a = kali(4, 6)
print('2 + (4*6) - 4 = ', jumlah(a, b))

print('===========================================')
print('#Nomor 5b')
from operation import *

a = jumlah(4, 7)
b = jumlah(6, -9)
print('(4 + 7)*(6 - 9) = ', kali(a, b))

print('===========================================')
print('#Nomor 5c')
from operation import *

a = bagi(jumlah(10, 2), jumlah(7, 5))
b = kurang(12, 34)
print('(10 + 2)/(7 + 5)/(12 - 34) = ', bagi(a, b))
