list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[2 : 7])
print(list[ : : ])
print(list[:])  #  list[0 : 8 : 1]  --->  List  from  indexes  0  to  7  in  steps  of  1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])
print(list[ : : 2])
print(list[1 : : 2])
print(list[ : : -2]) #  list[-1 : -9 : -2]  --->  List  from  indexes  -1   to  -8   in  steps  of  -2  i.e. ['Hyd' , None , 'Hyd' , 10.8]
print(list[-2 : : -2])
print(list[1 : 4])
print(list[-4 : -1])
print(list[3 : -3])
print(list[2 : -5])
print(list[-1:-5])