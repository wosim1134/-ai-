a = {
    'a':12,
    'b':23,
    'c':34
}

a['d'] = 45

del a['a']

print(a)
print(a.keys())
print(a.values())
print(a.items())
print(a.get('a', 'no'))
print(a['b'])

if 'b' in a:
    print(56)