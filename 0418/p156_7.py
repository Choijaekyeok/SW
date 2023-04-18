'''
2023-04-18
최재혁
3장 연습문제 7번
두 정수 입력 x>y -> x//y x<y -> x+y,x==y ->x*y
단, 나눈셈 몫 계산할 때 y는 0 안됨
#문제분석
    변수: x의값(jumsu1), y의값(jumsu2)
    수식: x > y (/), x < y (+), x==y(*)
#알고리즘
    1.문제분석
    2.논리(선택-중첩if)
        if x>y:
            if y!=0:
                x//y
        elif x==y:
            x+y
        else:
            x*y
    3.결과 출력
'''


jumsu1=int(input("x의 값을 입력하시요:"))

jumsu2=int(input("y의 값을 입력하시요:"))



if jumsu1>jumsu2:
    if jumsu2!=0:
        print(jumsu1//jumsu2)
elif jumsu1==jumsu2:
    print(jumsu1+jumsu2)
else:
    print(jumsu1*jumsu2)

    



