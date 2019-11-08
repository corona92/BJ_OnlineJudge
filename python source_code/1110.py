import sys
N=sys.stdin.readline()
N=int(N)
a=int(N/10)
b=N%10
newN=0
cycle=0
while N!=newN :
    newN=a+b
    cycle=cycle+1
    if newN >= 10 :
        a=b
        #b=newN%10
    else :
        newN=b*10+newN
        a=int(newN/10)
        #b=newN%10
    b=newN%10

print(cycle)
