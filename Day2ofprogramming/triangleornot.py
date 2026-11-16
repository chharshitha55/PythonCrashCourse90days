import math
s1=float(input('enter 1st side: '))
s2=float(input('enter 2nd side: '))
s3=float(input('enter 3rd side: '))

if(s1+s2>s3 and s2+s3>s1 and s1+s3>s2):
    if(s1==s2 and s2==s3):
        triangle='equilateral'
    elif(s1==s2 or s2==s3 or s3==s1):
        triangle='isoscles'
    elif(s1!=s2 and s2!=s3 and s3!=s1):
        triangle='scalene'
    print(triangle)
    
    if(triangle=='equilateral'):
        area=math.sqrt(3)/4*(s1**2)
        print('Area: ',F'{area:.2f}')
        
    elif(triangle=='isoscles'):
        perimeter=s1+s2+s3
        print('perimeter: ',perimeter)
        
    elif(triangle=='scalene'):
        s=(s1+s2+s3)/2
        area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
        print('Area: ',area)
        perimeter=s1+s2+s3
        print('perimeter: ',perimeter)
else:
    print('not a triangle')

