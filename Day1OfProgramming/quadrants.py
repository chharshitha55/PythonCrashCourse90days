a=eval(input('enter a tuple of (x-coordinate, y coordinate):'))
if(a[0]>0 and a[1]>0):
    print('1st quad')
elif(a[0]<0 and a[1]>0):
    print('2nd quad')
elif(a[0]<0 and a[1]<0):
    print('3rd quad')
else:
    print('4th quad')
