'''
2023-05-09
최재혁
#문제정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제분석
    변수-정수(num)합계(fac)
#알고리즘
    1.변수초기화
        num에 정수를 입력받는다
    2.논리(반복 for)
        fac=1
        for i in range (num,0,-1)
        fac= fac*i
'''

num=int(input("팩토리얼 숫자 입력:"))

fac=1

for i in range(num,0,-1):
    fac=fac*i

print("%d의 팩토리얼 값은:"%num, fac)
