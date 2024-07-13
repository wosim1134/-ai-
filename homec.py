import sys
input = sys.stdin.readline
a = input().strip()
b = len(a)
a = int(a)
c = a - b*9
d = []
e = ''
g = []

for i in range(c, a+1):
    if i > 0:
        for j in range(len(str(i))):
            d.append(int(str(i)[j]))
        f = i + sum(d)
        if a == f:
            d = list(map(str, d))
            for k in d:
                e += k
            e = int(e)
            g.append(e)
        d.clear()
        e = ''

if g == []:
    print(0)
else:
    print(min(g))