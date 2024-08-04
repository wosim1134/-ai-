import sys
input = sys.stdin.readline

a = int(input())
dict1 = {}
d = []
for i in range(a):
    b, c = input().split()
    dict1[b] = c
    if dict1[b] == 'leave':
        del dict1[b]

for i in dict1.items():
    d.append(i)
d.sort(key=lambda x: x[0])

for i in reversed(d):
    print(i[0])