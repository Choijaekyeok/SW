'''
2023-04-11
최재혁
if~elif~else
연산자에 따라 결과가 달라진다
'''

num1=int(input("첫번째 숫자:")) #첫번째 정수 입력
op=input("연산자 입력:") #연산자 입력
num2=int(input("두번째 숫자:")) #두번쨰 정수 입력

if op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*":
    print(num1 * num2)
else:
    print(num1/num2)
    