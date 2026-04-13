import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
num1 = []
num2 = []

for i in range(n):
    row = [[x] for x in input().strip()]
    grid.append(row)

for i in range(n):
    count = 0
    for j in range(m):
        if grid[i][j][0] == '#':
            count += 1
    
    if count != 0:
        num1.append(count)

for i in range(m):
    count = 0
    for j in range(n):
        if grid [j][i][0] == '#':
            count += 1
        
    if count != 0:
        num2.append(count)

if num1[0] < num1[-1] and num1[0] < num2[0]:
    print("UP")
elif num1[-1] < num1[0] and num1[-1] < num2[0]:
    print("DOWN")
elif num2[0] < num2[-1] and num2[0]< num1[0]:
    print("LEFT")
else:
    print("RIGHT")