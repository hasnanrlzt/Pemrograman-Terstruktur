th = input('Tahun   : ')
if (int (th) % 400) == 0:
    print('Tahun ', th , ' adalah Tahun Kabisat')
elif(int(th) % 400)!= 0:
    if int(th) % 100 == 0:
        print('Tahun ', th, ' bukan Tahun Kabisat')
    elif int(th) % 100 != 0:
        if int(th) % 4 == 0:
            print('Tahun ', th, ' adalah Tahun Kabisat')
        elif int(th) % 4 != 0:
            print('Tahun ', th, ' bukan Tahun Kabisat')
