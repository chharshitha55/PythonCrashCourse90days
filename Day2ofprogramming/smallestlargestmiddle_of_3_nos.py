n1=float(input("enter first no: "))
n2=float(input("enter 2nd no: "))
n3=float(input("enter 3rd no: "))

max=n1
if(n2>max):
    max=n2
elif(n3>max):
    max=n3
min=n1
if(n2<min):
    min=n2
elif(n3<min):
    min=n3
mid=(n1+n2+n3)-(max+min)

print('Largest input:',max)
print('Smallest input:',min)
print('Middle input:',mid)



