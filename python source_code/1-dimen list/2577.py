import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C= int(sys.stdin.readline())
mult_n=A*B*C
L=[0,0,0,0,0,0,0,0,0,0]
str_mult=str(mult_n)
for i in range(0,len(str_mult)) :
    L[int(str_mult[i])] = L[int(str_mult[i])]+1 # 0 이면 해당 index 값을 증가

for i in range(0,len(L)) :
    print(L[i])

