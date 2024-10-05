S =input()
test = S[::-1]

for i in range(len(S)):
    temp = S + test[len(S)-i:]

    if temp == temp[::-1]:
        print(len(S)+i)
        break