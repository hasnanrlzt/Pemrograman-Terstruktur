#diketahui jarak a ke c 795 km, konsumsi mobil 1l tiap 12 km
def BBM(jaraktempuh,jumlahbbm):
    return jaraktempuh/jumlahbbm

jaraktempuh= int(input('berapa km jarak dari kota A ke kota C? '))
jumlahbbm= int(input('berapa km jarak yang ditempuh dengan 1l BBM? '))
bbm= BBM(jaraktempuh,jumlahbbm)
print('===========================================================')
print('jumlah BBM yang diperlukan = ', bbm,'liter')