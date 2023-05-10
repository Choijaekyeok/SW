'''
2023-05-10
최재혁
#문제정의 
    3의 자리 배수를 값과 합계와 몇 번째 배수인가를 구하라
#문제분석
    변수-숫자(num) 합계 (sum) 입력횟수(cnt)
#알고리즘
    1.변수 초기화
        num변수에 정수를 입력받는다
    2.논리(반복)
        while True:
            i=i+3
            sum=sum+1
            cnt=cnt+1
            if sum>num:
                break
'''

num=int(input("사용자 입력:"))
sum=0
cnt=0
i=0
while True:
    i=i+3
    sum=sum+1
    cnt=cnt+1
    if sum>num:
        break
print("{}을 넘었을 때 숫자:{}".format(num,i))
print("{}을 넘었을 때 까지의 합계:{}".format(num,sum))
print("{}을 넘었을 때 까지 몇 번쨰 3의 배수인가".format(num,cnt))