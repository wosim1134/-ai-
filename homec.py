import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = list(map(int, input().split()))
d = 0

for i in range(a-2):
    for j in range(i+1, a-1):
        for k in range(j+1, a):
            e = c[i]+c[j]+c[k]
            if d <= e <= b:
                d = e
print(d)