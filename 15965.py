import math

k = int(input())
limit = 2000000 if k > 100 else 1000 

prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(limit)) + 1):
    for j in range(i * i, limit+1, i):
        prime[j] = False

count = 0
i = 2

while True:
    if prime[i]:
        count += 1
    
    if count == k:
        print(i)
        break
    
    i += 1