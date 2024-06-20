def aq(a):
    z = []
    for i in a:
        if type(i) == list:
            z += aq(i)
        else:
            z.append(i)
    return z







a = [1, [2, 3], [[4, 5], 6], [[[7]], 8, 9], [10]]
print(aq(a))
