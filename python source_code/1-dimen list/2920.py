import sys
L=sys.stdin.readline().split()
Input=[]
for i in range(0,len(L)) :
    Input.append(int(L[i]))

if Input == sorted(Input) :
    print("ascending")
elif Input == list(reversed(sorted(Input))) :
    print("descending")
else :
    print("mixed")
