import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = 0
a1 = [input().strip() for i in range(a)]
b1 = [input().strip() for i in range(b)]

for i in b1:
    if i in a1:
        c += 1
print(c)