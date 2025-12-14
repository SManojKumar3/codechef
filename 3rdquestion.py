t=int(input())
for i in range(t):
    n=int(input())
    ai=input().split()
    allcount=[]
    for q in range(n):
        c=0
        for j in range(n):
            f=[]
            for aa in range(n):
                if len(ai)>2:
                    if len(f)<2:
                        if ai[aa] not in f:
                            f.append(ai[aa])
                else:
                    f=ai
        for z in ai:
            if z in f:
                c+=1
            else:
                break
        allcount.append(c)
        ai.pop(0)
    print(max(allcount))
