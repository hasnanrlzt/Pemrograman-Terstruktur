try:
    file = open('d:/myfile.txt', 'r')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')

