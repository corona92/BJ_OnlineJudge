L=[1,2,3,4,5]
D=set(L)
try:
    a=int(input("리스트 L에 추가할 data를 입력 : "))
    L.append(a)
    L=list(set(L))
    if D == set(L) :
        print("이미 존재하는 데이터입니다.")

except ValueError :
    print("정수 숫자 데이터만 허용합니다.")

print(L)