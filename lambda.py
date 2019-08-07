l=(1,2,3,4,5)
l1 =tuple(map(lambda x : x-2,l))
print(l1)

print("=============================")
# filter
l=(1,2,3,4,5)

l1=tuple(filter(lambda x:(x%1==0),l))
print(l1)
print("=========================")
#reduce
from functools import reduce
l=(1,2,3,4,5)
l2=reduce(lambda x,y:x//y,l)
print(l2)
