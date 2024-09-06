a = 1
b = [2]
c = int(input()) # 소수 구하기
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

f = int(input()) # 진법
g = []
h = []
for i in b:
    while True:
        if i // f == 0:
            g.insert(0, i)
            break
        g.insert(0, i % f)
        i = i // f
    g = list(map(str, g))
    g = ''.join(g)
    g = int(g)
    h.append(g)
    g = []


print(h)
