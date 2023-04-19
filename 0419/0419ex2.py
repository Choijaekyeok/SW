'''
2023-04-19
최재혁
입력받은 숫자가 양수, 0 음수인지 판단
#문제분석
    변수- 정수(num)
    수식
        num>0 양수
        num<0 음수
        
#알고리즘 (단순 if)
    1.변수 선언
        num에 정수 입력
    2.논리(선택)
        if num>0:
            "양수"
        if num<0:
            "음수"
        if num==0:
            "0"
#알고리즘 (다중 if)
    1.변수 선언
        num에 wjdtn dlqfur
    2.논리 (선택)
        if num>0:
            "양수"
        elif num<0"
            "음수"
        else:
            0
'''
#단순 if
num=int(input("정수 입력:"))

if num>0:
    print("양수")
if num<0:
    print("음수")
if num==0:
    print("0")

#다중 if

if num>0:
    print("양수")
elif num<0:
    print("음수")
else:
    print("0")

