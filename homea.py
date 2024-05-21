a = int(input())
b = []
c = 0
for i in range(a):
    b.append(input())



print(b)

for i in range(len(b)):
    d = [0 for p in range(len(b[i]))]

    for j in range(len(b[i])-2):

        for k in range(j+2, len(b[i])):

            if b[i][j] == b[i][k]:

                if b[i][j] != b[i][j+1]:
                    
                    c += 1