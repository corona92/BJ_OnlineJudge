import sys
Formula_L=[]
N=int(sys.stdin.readline())
Formula=sys.stdin.readline()
result=0
for i in range(0,len(Formula)) :
    Formula_L.append(Formula[i])

result=int(Formula_L[0])
for i in range(0,len(Formula_L)) :
    if Formula_L[i] == '+' :
        result = result+int(Formula_L[i+1])
    elif Formula_L[i] == '-' :
        result = result-int(Formula_L[i+1])
    elif Formula_L[i] == '*' :
        result =
    elif Formula_L[i] == '/' :
        print("/")

print(result)

#resolve