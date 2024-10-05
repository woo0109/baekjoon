arr = []
total = 0

for i in range(5):
    arr.append(int(input()))
    total += arr[i]
arr.sort()

print(total//5)
print(arr[2])