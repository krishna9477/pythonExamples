#  Remove duplicates from a list
l1=[1,2,3]
l2=[10,8,2,3]
l3=l2.extend(l1)
print(l2)
l4=list(dict.fromkeys(l2))
print(l4)
l4.remove(3)
l4.remove(1)
print(l4)


