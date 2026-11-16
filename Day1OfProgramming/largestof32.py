a=eval(input('Enter 1st input: '))
b=eval(input('Enter 2nd input: '))
c=eval(input('Enter 3rd input: '))

if a>b and a>c:
    print('Largest Input:', a)
elif b>a and b>c:
    print('Largest Input:',b)
else:
    print(c)