l1=[1,2,3]
l2=[3,4,5]
l3=dict(zip(l1,l2))
print(l3)

print("===========")
l4=[1,2,3,1,2,3]
l5=list(dict.fromkeys(l4))
print(l5)
print("===============")
from collections import OrderedDict
str="list","tup","list",'tup',"str"
sw=",".join(OrderedDict.fromkeys(str))

print(sw)

from collections import OrderedDict
def removedup(s):
    return ",".join(OrderedDict.fromkeys(s))
print(removedup('python is a programing language'))


print("=====================")
lrt=[1,2,3,4,5]
if 5 in lrt:
    print('yes')
else:
    print('no')




print("====================================")

#closure

def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner

a=outer()
print(a())


print("===================================")

print("hello")



lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
print(lst)




