N = int(input())

array = [[0]*100 for i in range(100)]

for i in range(N):
    x, y = map(int, input().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            array[j][k] = 1

result = 0

for i in range(100):
    result += array[i].count(1)

print(result)