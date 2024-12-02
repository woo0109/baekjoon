A = int(input())
B = int(input())
C = int(input())

arr = [0] * 10

D = A * B * C

for i in range(len(str(D))):
    j = D % 10
    arr[int(j)] += 1
    D /= 10

for i in arr:
    print(i)