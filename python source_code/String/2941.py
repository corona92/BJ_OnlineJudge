import sys
S=sys.stdin.readline()
new_S=[]
index=0
for i in range (0,len(S)-1) :
    if index < len(S) :
        i=index
    else :
        break
    if S[i] == "\n" :
        break

    if S[i] == "l" :
        if S[i+1] =="j" :
            index=i+2
            new_S.append("lj")
        else :
            index=i+1
            new_S.append(S[i])
    elif S[i] == "c":
        if S[i+1] == "=" :
            index=i+2
            new_S.append("c=")
        elif S[i+1] == "-" :
            index=i+2
            new_S.append("c-")
        else:
            index=i+1
            new_S.append(S[i])
    elif S[i] == "d":
        if S[i+1] == "z":
            if S[i+2] == "=":
                index=i+3
                new_S.append("dz=")
        elif S[i+1] == "-":
            index=i+2
            new_S.append("d-")
        else:
            index=i+1
            new_S.append(S[i])
    elif S[i]=="n":
        if S[i+1] == "j":
            index=i+2
            new_S.append("nj")
        else:
            index=i+1
            new_S.append(S[i])
    elif S[i]=="s":
        if S[i+1] == "=":
            index=i+2
            new_S.append("s=")
        else:
            index=i+1
            new_S.append(S[i])
    elif S[i]=="z":
        if S[i+1]=="=":
            index=i+2
            new_S.append("z=")
        else:
            index=i+1
            new_S.append(S[i])
    else:
        index=i+1
        new_S.append(S[i])
print(len(new_S))