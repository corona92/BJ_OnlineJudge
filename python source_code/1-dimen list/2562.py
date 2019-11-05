import sys
In=[]
max_n=0
ind_n=0
for i in range(0,9) :
    In.append(int(sys.stdin.readline()))
    if max_n < In[i] :
        ind_n = i+1
    max_n=max(max_n,In[i])

print(max_n)
print(ind_n)

