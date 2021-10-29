def starFormation1(n):
    x = 0
    y = 0
    while (y <= n):
        z = 0
        while (z < x):
            print('* ', end='')
            z += 1
        x += 1
        print('')
        y += 1

def starFormation2(n):
    x = 4
    y = 0
    while (y < n):
        z = 0
        while (z < x):
            print('* ', end='')
            z += 1
        x -= 1
        print('')
        y += 1

def starFormation3(n):
    starFormation1(3)
    starFormation2(4)

starFormation1(4)
print('============================')
starFormation2(4)
print('============================')
starFormation3(7)

