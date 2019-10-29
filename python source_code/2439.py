import sys
a=sys.stdin.readline()
a=int(a)
b=(a-1)*2
p='*'
pp=''
for i in range(1,a+1) :
    pp=p*i
    print(pp.rjust(b))

#다시풀기
