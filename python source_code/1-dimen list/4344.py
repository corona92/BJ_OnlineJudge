import sys
C=int(sys.stdin.readline()) #testcase
sum=0
count=0
avg=0
num_avg=[]
for i in range(0,C) :
    inp = sys.stdin.readline().split() #student Number, score, score, score
    st_n= int(inp[0]) #student Number

    for j in range(1,len(inp)) :
        sum=sum+int(inp[j])

    avg=sum/st_n
    for k in range(1,len(inp)) :
        if avg < int(inp[k]) :
            count = count+1

    num_avg.append(round((count/st_n*100),3))
    sum=0
    count=0

for a in range(0,len(num_avg)):
    print('%.3f' % num_avg[a] + '%')


