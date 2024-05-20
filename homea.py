a = int(input())
b = [[i for i in input()] for j in range(a)]

for i in range(a):
    b[i].append(' ')

print(b)

for i in range(len(b)):
    for j in range(len(b[i])-1):
        if b[i][j] == b[i][j-1]:
            del b[i][j]
print(b)