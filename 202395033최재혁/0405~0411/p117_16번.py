'''
2023-04-05~2023-04-11
최재혁
최종 자동차 값 구하기 (p117-16)
'''


ctx=int(input('자동차 세금:')) #자동차 세금
amy=ctx*0.03 #가산금

total_fct=ctx+amy

print("자동차세금은 {}이고, 가산금이 {}일때 최종 자동차 세금은{}이다.".format(ctx,amy,total_fct))
