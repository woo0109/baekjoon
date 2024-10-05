import math

k = int(input())
count = 0
num = 2

while count<k:
    prime = True

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            prime = False
            
    if prime:
        count += 1
    num += 1

print(num-1)