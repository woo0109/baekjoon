import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = 0

for _ in range(n):
        h = int(input())

        while stack and stack[-1][0] < h:
            ans += stack.pop()[1]

        if not stack:
            stack.append([h, 1])
            
        else:
            if stack[-1][0] == h:
                cnt = stack.pop()[1]
                ans += cnt  
                
                if stack:
                    ans += 1
                
                stack.append([h, cnt + 1])
            
            else:
                ans += 1  
                stack.append([h, 1])

print(ans)