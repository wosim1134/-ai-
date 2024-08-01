import sys
import heapq

T = sys.stdin.readline

a = int(T())
b = list(map(int, T().split()))
c = [0] * a

min_heap = [(value, index) for index, value in enumerate(b)]
heapq.heapify(min_heap)

e = 0

while min_heap:
    mi, w = heapq.heappop(min_heap)
    if b[w] == mi:
        for i in range(a):
            if b[i] == mi:
                c[i] = e
                b[i] = float('inf')
        e += 1

print(*c)