a = int(input())
b = [tuple(map(int, input().split())) for i in range(a)]
print(b)
c = sorted(b, key=lambda point: (point[0], point[1]))
for i in c:
    print(f'{i[0]} {i[1]}')