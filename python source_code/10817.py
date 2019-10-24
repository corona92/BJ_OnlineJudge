A, B, C = input().split()
A=int(A)
B=int(B)
C=int(C)


if A > B :
    #A B C
    if B > C :
        print(B)
    else :
        # C A B
        if C > A :
            print(A)
        # A C B
        else :
            print(C)

# B > A
else :
    # C B A
    if C > B :
        print(B)
    # B > C
    else :
        if C > A :
            print(C)
        
        else :
            print(A)
