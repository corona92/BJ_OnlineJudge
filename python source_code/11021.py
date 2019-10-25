import sys
N=sys.stdin.readline()
N=int(N)
sum_a=[]

for i in range(0,N) :
    a,b=map(int, sys.stdin.readline().split())
    sum_a.append(a+b)

for i in range(0,len(sum_a)) :
    print("Case #%d: %d" % (i+1, sum_a[i]))
