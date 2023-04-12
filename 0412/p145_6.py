'''
2023-04-12
최재혁
두 정수 입력 후
모두 짝수이면 더한값 출력
모두 홀수이면 "두 숫자 모두 짝수로 입력하세요"출력
하나만 홀수이면 "몇 번째 정수를 짝수로 입력하세요" 출력
#문제분석
    변수- 정수1(num1), 정수2(num2)
    수식- num1%2==0 and num2%2==0: (num1+num2은 짝수)
          num1%2==0 and num2%2==1: (num2는 홀수), num1%2==1 and num2%2==0:(num1은 홀수)
          num1%2==1 and num2%2==1: (num1과 num2는 모두 홀수)
#알고리즘
    1.변수선언
    2.논리(선택 if~elif~else)
        if num1%2==0 and num2%2==0: 
            (조건1 )"num1 + num2"
        elif num1%2==0 and num2%2==1 or num1%2==1 and num2%2==0:
            (조건 2)"몇번째 정수를 짝수로 입력하세요"
        else:
            "두 숫자 모두를 짝수로 입력하세요"
'''

num1=int(input("첫 번째 정수 입력:"))
num2=int(input("두 번째 정수 입력:"))

if  num1%2==0 and num2%2==0:
    print (num1,"+",num2,"=",num1+num2)
elif num1%2==1 and num2%2==0: 
    print ("첫 번째 숫자를 정수로 입력하세요")
elif num1%2==0 and num2%2==1:
    print ("두 번째 숫자를 정수로 입력하세요")
else:
    print ("두 숫자 모두를 짝수로 입력하세요")