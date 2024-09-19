import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c = [input().rstrip() for i in range(a)]
d = [input().rstrip() for i in range(b)]
e = []

c = sorted(c, key=lambda x: x)
d = sorted(d, key=lambda x: x)

