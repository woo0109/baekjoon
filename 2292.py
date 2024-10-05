a = int(input())
i=0
b = a-1

while True:
    b -= 6*i
    if b <= 0:
        break
    i+=1

print(i+1)