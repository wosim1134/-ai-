a, b = input().split()
b = int(b)
c = 0

for i in range(1, len(a)+1):
    if '0' <= a[-i] <= '9':
        c += (ord(a[-i]) - ord('0')) * b ** (i - 1)
    else:
        c += (ord(a[-i]) - 55) * b ** (i - 1)

print(c)