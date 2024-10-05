m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    e = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                e += 1
                break
        if e == 0:
            list.append(i)

if len(list) > 0:
    print(sum(list))
    print(min(list)) 
else:
    print("-1")