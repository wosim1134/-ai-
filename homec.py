a = int(input())
b = [tuple(map(int, input().split())) for i in range(a)]

c = sorted(b, key=lambda point: (point[0], point[1]))
print(c)