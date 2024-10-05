word = input().upper()
wlist = list(set(word))
clist = []

for i in wlist:
    count = word.count(i)
    clist.append(count)

if clist.count(max(clist)) >= 2:
    print("?")

else:
    print(wlist[clist.index(max(clist))])