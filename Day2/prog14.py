# complex()  function  demo  program
print(complex(3 , 4))#3+4j
print(complex(0 , 4))#0+4j
print(complex(3))#3+0j
print(complex(3.8 , 4.6))#3.8+4.6j
print(complex(3.8))#3.8+0j
print(complex(3 , 4.5))#3+4.5j
print(complex(True , False))#1+0j
print(complex(True))#1+0j
print(complex(False))#0j
print(complex(True , 4))#1+4j
print(complex('3'))#3+0j
print(complex('3.8'))#3.8+0j
# print(complex(3 , '4'))  #imag can't be string 
# print(complex('3' , 4))  #when 1st arg is str it cant have imag
# print(complex('3' , '4')) #when 1st arg is str it cant have imag
# print(complex('Ten'))