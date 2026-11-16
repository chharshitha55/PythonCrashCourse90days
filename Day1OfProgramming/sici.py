p=float(input('Enter principle : '))
t=float(input('Enter time : '))
r=float(input('Enter rate of interest : '))
si=(p*t*r)/100
ci=p*(1+r/100)**t-p
print('Simple Interest : ',F'{si:.2f}')
print('Compound Interest : ',F'{ci:.2f}')
