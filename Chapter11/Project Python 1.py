from datetime import *
try:
    def diffDate(x):
        tanggal = datetime.date(datetime.now())
        print('Tanggal hari ini                          :',tanggal)
        year, month, day = x.split('-')
        searchtgl = date(int(year), int(month), int(day))
        selisih = tanggal - searchtgl
        selisihHari = abs(selisih.days)
        return selisihHari

    print('='*55)
    x = str(input('Masukkan tanggal dengan format YYYY-MM-DD : '))
    print('='*55)
    print('Selisih hari  adalah                      :',diffDate(x), ' hari')
except ValueError:
    print('Selisih tidak dapat diproses karena input tidak valid !!!!!')

