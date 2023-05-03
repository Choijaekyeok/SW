'''
2023-05-03
최재혁
1~10까지 합계 구하기
'''

#while
i=1  #반복횟수 초기화
sum=0 #합계
while i<=10: #반복 조건
    sum=sum+i #합계 저장
    i=i+1
print('1~10까지의 합계:',sum)


print()
#for반복

sum1=0
for t in range(1,101):
    sum1=sum1+t #합계 저장
print('1~10까지 합계:',sum1)
