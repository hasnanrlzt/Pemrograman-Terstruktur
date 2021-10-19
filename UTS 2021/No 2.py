from random import randint
print("Level:")
print("1 Level 1 (Penjumlahan)")
print("2 Level 2 (Pengurangan)")
print("3 Level 3 (Perkalian)")
print("4 Exit")
level = input("Pilih Level : ")
lives = 3
score = 0
while True:
    if int(level) == 1:
        if lives > 0:
            x = randint(-100, 100)
            y = randint(-100, 100)
            jwb = x + y
            jwbpemain = input("Hasil (" + str(x) + ") + (" + str(y) + ") = ")
            if int(jwbpemain) == jwb:
                score += 2
                print()
                print("Yeayyy...benar!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
            else:
                lives -= 1
                score -= 2
                print()
                print("Yahhh...salah!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
        else:
            print("Game Over")
            break
    elif int(level) == 2:
        if lives > 0:
            x = randint(-100, 100)
            y = randint(-100, 100)
            jwb = x - y
            jwbpemain = input("Hasil dari (" + str(x) + ") - (" + str(y) + ") = ")
            if int(jwbpemain) == jwb:
                score += 2
                print()
                print("Yeayyy...benar!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
            else:
                lives -= 1
                score -= 2
                print()
                print("Yahhh...salah!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
        else:
            print("Game Over")
            break
    elif int(level) == 3:
        if lives > 0:
            x = randint(-100, 100)
            y = randint(-100, 100)
            jwb = x * y
            jwbpemain = input("Hasil dari (" + str(x) + ") x (" + str(y) + ") = ")
            if int(jwbpemain) == jwb:
                score += 2
                print()
                print("Yeayyy...benar!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
            else:
                lives -= 1
                score -= 2
                print()
                print("Yahhh...salah!!! Score Anda =" + str(score) + " (Lives :" + str(lives) + ")")
        else:
            print("Game Over")
            break
    elif int(level) == 4:
        break
    else:
        print('Maaf pilihan anda salah')
        break
