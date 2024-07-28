a = int(input())
b = [list(map(int, input().split())) for i in range(a)]

for i in range(a-1):
    for j in range(i, a):
        if b[i][0] >= b[j][0]:
            b[i], b[j] = b[j], b[i]
        if b[i][0] == b[j][0] and b[i][1] > b[j][1]:
            b[i], b[j] = b[j], b[i]
print(b)