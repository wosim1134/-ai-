import sys
input = sys.stdin.readline

Num = []
Num_dict = {}

Count1 = int(input())
Number1 = list(map(int, input().split()))
Count2 = int(input())
Number2 = list(map(int, input().split()))
Number_1 = sorted(set(Number1))
Number_2 = sorted(set(Number2))

a = 0
b = 0

print(Number1)
print(Number2)
print(Number_1)
print(Number_2)

while a <= Count1 and b <= Count2:
    if Number_1[a] == Number_2[b]:
        Num_dict[Number_2[b]] = 1
    

    a += 1
    b += 1
print(Num_dict)