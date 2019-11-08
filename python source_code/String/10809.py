import sys
S=sys.stdin.readline()
L=[-1]*26
for i in range(0,len(S)-1) :
    if L[ord(S[i])-97] == -1 :
        L[ord(S[i])-97] = i

print(" ".join(str(i) for i in L))

    # a = 97 ~ z = 122