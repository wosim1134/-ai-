import math
A, B, V = map(int, input().split())
C = A - B

m = math.ceil((V-A)/C +1)
print(m)