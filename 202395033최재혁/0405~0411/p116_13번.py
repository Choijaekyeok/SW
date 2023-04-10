'''
2023-04-05~2023-04-11
최재혁
패밀리 레스토랑에서 저녁 식사 값 구하기 (p116-13)
'''

pay=int(input('음식 요금:')) #음식 요금 
vat=pay*0.1 #부가세 

total_prm=pay+vat

print("음식 요금은 {}이고, 부가세가 {}일때 지불 식사 금액은{}이다.".format(pay,vat,total_prm))
