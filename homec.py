import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())

y = (c*d-a*f) / (b*d-a*e)
x = (-b*y+c)/a
print(int(x), int(y))