xl = []
yl = []

for i in range(3):
    x, y = map(int, input().split())
    xl.append(x)
    yl.append(y)

for i in range(3):
    if xl.count(xl[i]) == 1:
        x4=xl[i]
    if yl.count(yl[i]) == 1:
        y4=yl[i]

print(x4, y4)