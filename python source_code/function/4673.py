L=[]
def d(n) :
    num=0
    L.append(n)
    while num < 10000 :
        num = int(n/10) + int(n) + int(n%10)
        if num > 10000 :
            break
        L.append(num)
        n=num
    return num

print(d(33))
print(L)