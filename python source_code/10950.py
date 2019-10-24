#testcase
t=input()
t=int(t)
a= []

for i in range(1,t+1) :
    ina, inb = input().split()
    ina = int(ina)
    inb = int(inb)
    a.append(ina+inb)

for i in range(0,t) :
    print(a[i])
