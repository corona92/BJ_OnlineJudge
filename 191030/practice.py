list_input=[]
Input=input("Enter a sentence : ").split()
for i in Input :
    list_input.append(i)
ND=sorted(list(set(list_input)))
print("Non duplicate words (list) : ", ND)
print("Non duplicate words (string) : ", '_'.join(ND))
