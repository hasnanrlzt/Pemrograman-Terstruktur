def buahMahal():
    data= {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
    x = list(data.values())
    x.sort(reverse=True)
    max = x[0]
    for data, x in data.items():
        if x == max:
            print(data,max)
buahMahal()

