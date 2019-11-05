import sys
N=int(sys.stdin.readline()) # N
Input=sys.stdin.readline().split() # 1 2 3 4 5
max_num=0
min_num=int(Input[0])
for i in range(0, len(Input)) :
   max_num=max(max_num,int(Input[i]))
   min_num=min(min_num,int(Input[i]))

print(min_num, max_num)