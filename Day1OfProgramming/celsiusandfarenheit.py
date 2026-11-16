temp=int(input('enter 1 to convert celsius to farenheit and 2 to convert to celsius : '))
if(temp==1):
    celsius=float(input('enter celsius temperature:'))
    res=1.8*celsius+32
    print('farenheit equivalent:',F'{res:.2f}')
elif(temp==2):
    farenheit=float(input('enter farenheit temperature:'))
    res=(farenheit-32)/1.8
    print('celsius equivalent:',F'{res:.2f}')
else:
    print('invalid input')