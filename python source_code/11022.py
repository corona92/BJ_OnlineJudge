import sys
N=sys.stdin.readline()
N=int(N)
sum_a=[]
inta=[]
intb=[]

for i in range(0,N) :
    a,b=map(int, sys.stdin.readline().split())
    inta.append(a)
    intb.append(b)
    sum_a.append(a+b)

for i in range(0,len(sum_a)) :
    print("Case #%d: %d + %d = %d" % (i+1, inta[i], intb[i], sum_a[i]))
