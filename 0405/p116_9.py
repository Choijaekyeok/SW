'''
2023-04-05
최재혁
이번달 수령액 구하기 (p116-9)
'''

bbg=int(input('본봉:')) #본봉 점수 입력
epy=int(input('수당:')) #수당 점수 입력
tax=(bbg+epy)*0.2 #세금 계산

total_bbg=bbg+epy-tax #수령액 계산

print("본봉이 {}이고, 수당이 {}일때 실수령액은 {}이다.".format(bbg,epy,total_bbg))