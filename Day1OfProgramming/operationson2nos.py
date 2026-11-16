import math
n1=int(input('Enter 1st integer number : '))
n2=int(input('Enter 2nd integer number : '))
add=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2
rem=n1%n2
maxi=max(n1,n2)
mini=min(n1,n2)
power=pow(n1,n2)
square_root=math.sqrt(n1)
gcd=math.gcd(n1,n2)
facto=math.factorial(n1)
print(F'{n1} + {n2} = ', add)
print(F'{n1} - {n2} = ',sub)
print(F'{n1} * {n2} = ',mul)
print(F'{n1} / {n2} = ',div)
print(F'{n1} % {n2} = ',rem)
print(F'max({n1} , {n2}) = ',maxi)
print(F'min({n1} , {n2}) = ',mini)
print(F'{n1} ^ {n2} = ',power)
print(F'sqrt({n1}) = ',square_root)
print(F'gcd({n1} , {n2}) = ',gcd)
print(F'fact({n1}) = ',facto)


# Enter 1st integer number : 10
# Enter 2nd integer number : 7
# 10 + 7 =  17
# 10 - 7 =  3
# 10 * 7 =  70
# 10 / 7 =  1.4285714285714286
# 10 % 7 =  3
# max(10 , 7) =  10
# min(10 , 7) =  7
# 10 ^ 7 =  10000000
# sqrt(10) =  3.1622776601683795
# gcd(10 , 7) =  1
# fact(10) =  3628800