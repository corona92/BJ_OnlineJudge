import sys
def solve(a:list) :
    sum=0
    for i in range(0,len(a)):
        sum=sum+a[i]

    return sum

N=sys.stdin.readline().split()
List=[]
for i in range(0,len(N)) :
    List.append(int(N[i]))

print(solve(List))
