import sys
input = sys.stdin.readline

a = int(input())
b = [list(input().split()) for i in range(a)]

for i in range(a):
    b[i][0] = int(b[i][0])
    b[i].append(i)

b.sort(key=lambda x: (x[0], x[2]))

for i in b:
    print(f'{i[0]} {i[1]}')