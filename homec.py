import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [input().rstrip() for i in range(n)]
b = ['BWBWBWBW', 'WBWBWBWB'] * 4
c = ['WBWBWBWB', 'BWBWBWBW'] * 4
d = e = 0
h = 100

for i in range(n-7):
    for j in range(m-7):
        d = e = 0
        for k in range(8):
            for l in range(8):
                if a[k+i][l+j] != b[k][l]:
                    d += 1
                if a[k+i][l+j] != c[k][l]:
                    e += 1
        h = min(d, e, h)

print(h)