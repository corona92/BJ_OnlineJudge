import sys
n=input()
n=int(n)
a=[]
sum_a=[]
for i in range(0,n) :
    a,b =map(int, sys.stdin.readline().split())
    sum_a.append(a+b)

for i in range(len(sum_a)) :
    print(sum_a[i])
