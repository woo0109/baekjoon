n = int(input())

for i in range(1,n+1):
    nums = list(map(int, str(i)))
    if i+sum(nums) == n:
        print(i)
        break
    if i == n:
        print(0)