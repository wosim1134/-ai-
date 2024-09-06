a = 1
b = [2]
c = int(input())
d = 0
while True:
    a += 1
    d = 0
    if c == a:
        break

    for i in range(len(b)):
        if a % b[i] == 0:
            break
        else:
            d += 1
            if d == len(b):
                b.append(a)


print(b)
