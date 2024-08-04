import sys
input = sys.stdin.readline

a, b = map(int, input().split())

pokemon = {}
name_to_index = {}
for i in range(a):
    name = input().strip()
    pokemon[i + 1] = name
    name_to_index[name] = i + 1

for _ in range(b):
    q = input().strip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(name_to_index[q])