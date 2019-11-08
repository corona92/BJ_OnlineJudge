import sys
V=sys.stdin.readline()
l=[0]*26
MAX_NUM_l=0
index_l=0
check_error=0
for i in range(0,len(V)-1) :
    if ord(V[i])-97 >= 0 :
        l[ord(V[i])-97] = l[ord(V[i])-97]+1
        if l[ord(V[i])-97] > MAX_NUM_l :
            MAX_NUM_l=l[ord(V[i])-97]
            index_l=ord(V[i])-97

    else :
        l[ord(V[i])-65] = l[ord(V[i])-65]+1
        if l[ord(V[i])-65] > MAX_NUM_l :
            MAX_NUM_l=l[ord(V[i])-65]
            index_l=ord(V[i])-65

for i in range(0,len(l)-1) :
    if l[i] == MAX_NUM_l:
        if index_l != i :
            check_error=1

if check_error == 1:
    print("?")
else:
    print(chr(index_l+65))

# A=65 Z=90 a=97