import math
a=eval(input('enter tuple of (x co-ordinate, y co-ordinate): '))
x,y=a
b=float(input('enter radius of circle: '))
dist=math.sqrt(x**2 + y**2)

if(dist>b):
    print('point is outside of circle')
elif(dist<b):
    print('point is inside circle')
elif(dist==b):
    print('point is on the circle')