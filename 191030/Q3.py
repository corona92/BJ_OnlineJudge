m1=input("첫번째 문자열을 입력: ")
m2=input("두번째 문자열을 입력: ")
if sorted(m1) == sorted(m2) :
    print(m1+", "+m2+"는 anagram입니다.")
else :
    print(m1+", "+m2+"는 anagram이 아닙니다.")