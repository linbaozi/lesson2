import math
def quadratic(a,b,c):
    det=b*b-4*a*c
    if det>0:
        x1=(-b+math.sqrt(det))/(2*a)
        x2=(-b-math.sqrt(det))/(2*a)
        print('the one answer is %f'%x1)
        print('the second answer is %f'%x2)
    elif det==0:
        x=-b/(2*a)
        print('the only answer is%f'%x)
    else:
        print('NO SOULUTION')

print('input a b c')
a=float(input())
b=float(input())
c=float(input())
quadratic(a,b,c)

