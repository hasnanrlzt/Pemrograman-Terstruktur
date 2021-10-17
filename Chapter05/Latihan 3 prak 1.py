print('Nilai Bahasa Indonesia :')
bi = int(input())
print("Nilai IPA  :")
ipa = int(input())
print('Nilai Matematika :')
mtk = int(input())


if bi >=0 and bi <=100 and ipa >=0 and ipa <=100 and mtk >=0 and mtk <=100:
        #print("Valid")
    if bi >=60 and bi <=100 and ipa >=60 and ipa <100 and mtk >=70 and mtk <=100:
        print("Lulus")
    else:
        print('Tidak Lulus')
        if bi <60:
            print('Nilai Bahasa Indonesia <60')
        if ipa <60:
            print('Nilai Ipa <60')
        if mtk <70:
            print('Nilai Matematika <60')

else:
    print("Terdapat nilai tidak valid")