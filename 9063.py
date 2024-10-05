n = int(input())
xl = []
yl = []

for i in range(n):
    x, y = map(int,input().split())
    xl.append(x)
    yl.append(y)

xr=max(xl)-min(xl)
yr=max(yl)-min(yl)

print(xr*yr)