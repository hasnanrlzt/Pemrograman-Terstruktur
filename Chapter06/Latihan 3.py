# Rumus Combinasi = n! / (n - k)! x k!
# Rumus Permutasi = n! / (n -k) !
# Keterangan : (n = nilai) (k = kriteria)
def faktorial(n):
    faktorial = 1
    while (n > 0):
        faktorial = faktorial * n
        n -= 1
    return faktorial

# Function Combinasi
def Combinasi(n, k):
    C = faktorial(n) / faktorial(n - k) * faktorial(k)
    return C

nilai = 5
kriteria = 3
print('Kombinasi dari C(' , nilai , ', ', kriteria , ') = ',Combinasi(nilai, kriteria))

# Function Permutasi
def Permutasi(n, k):
    P = faktorial(n) / faktorial(n - k)
    return P

nilai = 10
kriteria = 7
print('Permutasi dari P(', nilai , ', ', kriteria , ') = ', Permutasi(nilai, kriteria))

