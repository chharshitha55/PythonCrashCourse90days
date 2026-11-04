# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))
print(a)
print(*a)
print(id(a))
print(len(a))
print(*a[2 : 7] , sep = ' , ')
print(*a[ : : -1])
# a[4] = 32 range is immutable
# print(a * 2) range cant be multipied