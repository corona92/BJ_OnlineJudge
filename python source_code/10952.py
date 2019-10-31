import sys
A=1
B=1
sum=[]
while A!=0 :
    A, B = map(int,sys.stdin.readline().split())
    sum.append(A+B)
i=0

while i!=(len(sum)-1) :
    print(sum[i])
    i=i+1