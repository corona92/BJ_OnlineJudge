import sys
N=int(sys.stdin.readline())
S=sys.stdin.readline()
sum=0
for i in range(0,len(S)-1):
    sum=sum+int(S[i])
print(sum)
