a, b = map(int, input().split())
c = 0
d = 0

while True:
    c = a % b
    a = a // b
    if 0 <= c <= 9:
