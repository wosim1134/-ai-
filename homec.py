# 입력값
# z3 234 30
# z2 123 10
# z1 345 20
# 1 3
# 5 8
# 2 3

class c1:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def __lt__(self, other):
        return self.height < other.height
    def pin(self):
        print('%s, %.2f, %.2f' % (self.name, self.height, self.weight))

def name(self):
    return self.name

def weight(self):
    return self.weight

def inp2():
    a = []
    b = []
    for i in range(3):
        a.append(input().split())
        b.append(c1(str(a[i][1]), int(a[i][2]), int(a[i][3])))
    return b

def oup(a):
    for i in a:
        i.pin()

sa1 = inp2()
print('before')
oup(sa1); print()

print('height')
sa1.sort()
oup(sa1)

print('name')
sa1.sort(key = name)
oup(sa1)

print('weight')
sa1.sort(key = weight)
oup(sa1)

class c2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return c2(x, y)
    def __truediv__(self, other):
        return c2(self.x / other, self.y / other)
    def prn(self):
        print('%.2f, %.2f' % (self.x, self.y))

def inp1():
    a = []
    b = []
    for i in range(3):
        a.append(input().split())
        b.append(c2(int(a[i][1]), int(a[i][2])))
    return b

save = inp1()
su = save[0] + save[1] + save[2]
su /= 3
su.prn()