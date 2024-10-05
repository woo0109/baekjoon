b, n = input().split()
num ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = b[::-1]
sum = 0

for i in range(len(b)):
    sum += (int(n)**i)*num.index(b[i])

print(sum)