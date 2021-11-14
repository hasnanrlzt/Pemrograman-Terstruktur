try:
    x = int(input('Banyak bilangan yang diinginkan  : '))
    y = 0
    data =[]
    for y in range (x):
        z = int(input('Masukkan bilangan bulat : '))
        data += [z]
    data.sort(reverse = True)
    print(data)
except ValueError:
    print('Bukan merupakan bilangan bulat')

