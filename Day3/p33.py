# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a)
# How  to  print  dictionary  with  print()  function

print('Keys  of  dictionary')
for x in a.keys():
    print(x)
# How  to  iterate  thru  each  key  of  dict  'a'  with  for  loop
print('Values  of  dictionary')
for x in a.values():
    print(x)
# How  to  iterate  thru  each  value  of  dict  'a'  with  for  loop
print('Tuples  of  dict_items   object')
for x in a.items():
    print(x)
# How  to  iterate  thru  each  tuple  of  dict  'a'  with  for  loop
print('Elements  of  each   tuple')
for x in a.items():
    print(*x)
print('Another way to print elements of each tuple')
for x,y in a.items():
    print(x,y)
# How  to  print  elements  of  each  tuple  in  the  list  of  dict_items  object
print('Keys  and  values  of  dictionary')
for x in a.keys():
    print(x,a[x],sep=':')
# How  to  print  each  key  and  corresponding  value  in  dict  'a'