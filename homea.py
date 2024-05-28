a, b = map(int, input().split())
c = 0
d = []

while True:
    c = a % b
    a = a // b
    if 0 <= c <= 9:
        d.insert(0, c)
    else:
        d.insert(0, chr(c+55))
    if a == 0:
        for i in range(len(d)):
            print(d[i], end = '')
        break