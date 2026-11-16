try:
    x=int(input('enter month number (1-12): '))

    if x>=1 and x<=12:
        if x==1:
            print('january')
        elif x==2:
            print('february')
        elif x==3:
                print('march')
        elif x==4:
                print('april')
        elif x==5:
                print('may')
        elif x==6:
                print('june')
        elif x==7:
                print('july')
        elif x==8:
                print('august')
        elif x==9:
                print('september')
        elif x==10:
                print('october')
        elif x==11:
                print('november')
        elif x==12:
                print('december')
    else:
        print('input should be between 1 and 12')
except ValueError:
    print("input should be an integer")
