import math
a=float(input("enter value of a: "))


if(a==0):
    print('value of a cannot be zero')
else:
    b=float(input("enter value of b: "))
    c=float(input("enter value of c: "))

    disc=b**2-4*a*c
    
    if(disc>0):
        print('roots are real and distinct')
        r1=(-b+math.sqrt(disc))/(2*a);
        r2=(-b-math.sqrt(disc))/(2*a);
        print(F'Root1:,{r1:.2f}')
        print(F'Root1:,{r2:.2f}')
    elif(disc==0):
        print('roots are real and equal')
        r1=-b/(2*a)
        r2=-b/(2*a)
        print('Root1:',r1)
        print('Root2:',r2)
    elif(disc<=0):
        print('roots are complex or imaginary')
        r1=-b/(2*a)
        print('Root1:',r1)
        r2=math.sqrt(-disc)/(2*a)
        print('Root1:',complex(r1,r2))
        print('Root2:',complex(r1,-r2))

     
     