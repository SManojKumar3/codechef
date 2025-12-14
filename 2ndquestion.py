n=int(input())
def find(v):
    z=1
    y=int(v[0])
    for j in range(len(v)-1):
        s=int(v[j+1])/y*z
        z=s
        y=int(v[j+1])
    return s    
    
import itertools

def get_all_arrangements(input_list):
    all_perms = list(itertools.permutations(input_list))
    return all_perms



for i in range(n):
    n2=int(input())
    g=input().split()
    all_arrangement=get_all_arrangements(g)
    check=False
    for e in all_arrangement:
        f=find(e)
        if f==1:
            check=True
    if check==True:
        print("YES")
    else:
        print("NO")
