a = int(input())
n = 0
while True:
    if a % 5 == 0 and a != 0:
        n += (a // 5)
        break
    a -= 3
    n += 1
    if a == 0:
        break
    elif a < 0:
        n = -1
        break
print(n)