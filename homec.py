a0, a1 = map(int, input().split())
c = int(input())
d = int(input())

if (a0 - c) * d + a1 <= 0 and a0 <= c:
    print(1)
else:
    print(0)


# a0n + a1 <= cn

# (a0 - c)n + a1 <= 0, n >= d
#
# c == a0:  a1 == 0, d = X
#
# c > a0:  d >= a1
#
#
#
#