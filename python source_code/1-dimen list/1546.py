import sys
N=int(sys.stdin.readline())
L=sys.stdin.readline().split()
score=[]
M=0 # Maximum number
sum=0
for i in range(0,len(L)) :
    M=max(M, int(L[i]))

for i in range(0,len(L)) :
    score.append(int(L[i])/M*100)
    sum=sum+score[i]

print(round(sum/len(L),6))  # new average
