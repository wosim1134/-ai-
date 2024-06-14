while True:
    a = int(input())
    if a == -1:
        break
    b = 0
    c = []
    if a > 0:
        for i in range(1, a):
            if a % i == 0:
                b += i
                c.append(i)

        if a == b and a > 0:
            print(f'{a} = 1', end = '')
        for i in range(1, len(c)):
            print(f' + {c[i]}', end = '')
    else:
        print(f'{a} is NOT perfect.')