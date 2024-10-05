max = 0
num = 0
for i in range(0,9):
    a = int(input())
    if a > max:
        max = a
        num = i
print(max)
print(num)