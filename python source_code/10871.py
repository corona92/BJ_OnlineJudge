import sys
N,X=sys.stdin.readline().split()
N=int(N)
X=int(X)

a=list(map(int,sys.stdin.readline().split()))
b=[]
for i in range(0, N) :
    if a[i] < X :
        b.append(a[i])

print(" ".join([str(i) for i in b]))