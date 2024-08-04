import sys
input = sys.stdin.readline

a, b = map(int, input().split())
pokemon = {}
c = []
for i in range(a):
    pokemon[i+1] = input().strip()

for i in range(b):
    q = input().strip()
    try:
        c.append(int(q))
    except:
        c.append(q)

w = list(pokemon.values())

for i in c:
    if type(i) == int:
        print(pokemon[i])
    elif type(i) == str:
        print(w.index(i) + 1)