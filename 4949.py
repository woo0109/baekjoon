while(True):
    S = input()
    if S[0] == '.':
        break
    tmp = []

    for i in S:
        if i == '(' or i == '[':
            tmp.append(i)
        elif i == ')':
            if len(tmp) != 0 and tmp[-1] == '(':
                tmp.pop()
            else:
                tmp.append(i)
                break
        elif i == ']':
            if len(tmp) != 0 and tmp[-1] == '[':
                tmp.pop()
            else:
                tmp.append(i)
                break
        
    if len(tmp) == 0:
        print("yes")
    else:
        print("no")