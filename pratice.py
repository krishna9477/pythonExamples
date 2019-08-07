# list to dict conversion
L1=[1,2,34,'string',5,'python']
L2=['program','palindrome','armstrong','fact']
d1=dict(zip(L2,L1))
print(d1)
print("======================================")
#list to remove duplicates.
p1=[1,2,34,'string',5,'python',2,34,34,1,5,'string']
p2=list(dict.fromkeys(p1))
print(p2)

print("======================================")
#string to remove duplicates.
from collections import OrderedDict
s="string","python","remove","string","python","remove"
s1="".join(OrderedDict.fromkeys(s))
print(s1)

#string to remove duplicates by using Function.

from collections import OrderedDict
def reverse(a):
    return "".join(OrderedDict.fromkeys(a))
print(reverse("python is a program for a string of numbers"))

print("======================================")

# List remove method

L1=[1,2,34,'string',5,'python']
L2=L1.reverse()
print(L1)

# List remove method by using Slice operator
L1=[1,2,34,'string',5,'python']
print(L1[::-1])

print("======================================")

# Tuple to Dict Conversion
t0=(1,2,34,'string',5,'python')
t1=(1,2,34,'string',5,'python')

t2=dict(zip(t0,t1))
print(t2)

print("======================================")

# how to search the no of elements from  a list
t0=[1,2,1,2,34,'string',5,'python']
y=[1,2,1,2,34,'string',5,'python']
t1=t0.index(34)
print(t1)

t1=len(t0)
print(t1)

t1 =t0.count(1)
print(t1)

t2=t0.append(y)

print(t0)

print(t0[8][3])

print("============================")

w1=[1,2,5,1,2,34]
w1.sort(reverse=True)
print(w1)
print("Good")
w2=w1.sort()
print(w1)
w3=w1.reverse()
print(w1)
print(w1[::-1])


print("==============================")
# find the 2nd largest element
q1=[1,2,5,1,2,34]
q2=q1.sort()
print(q1)
print("the 2nd largest element:",q1[-2])

print("==================================")

st=["string","banana","apple",'everest','cat','fcuk']
print(type(st))
st.sort(key=str.lower)
print(st)


t=["String","Banana","Apple",'Everest','Cat','Fcuk']
t.sort(key=str.upper)
print(t)


print("==================================")
le=[1,2,3,4,5,[6,7,8,9,10],'string','str','list']
print(le)

print("==================================")
#Type conversions

a=10
print(type(a))
b=str(a)
print(type(b))

""" 
a1='str'
print(type(a1))
b1=int(a1)
print(b1)
# output : valueError because when we are converting str to int it must and should be a number.
"""
print("Okay")
f1='26'
print(type(f1))
f2=int(f1)
print(type(f2))

f3=float(f1)
print(type(f3))

f4=complex(f1)
print(type(f4))

f5=bool(f1)
print(type(f5))
print("All are okay")
print("youuuuuuuuuuuuuuu")

o=12
ds=str(o)
print(type(ds))

ds1=complex(o)
print(ds1)
print(type(ds1))

ds2=float(o)
print(type(ds2))

ds3=bool(o)
print(ds3)
print(type(ds3))

print("==========================")
#implict

a=10
b=10.8
c=a+b
print(type(c))

print("============================")


ste=[1,2,4,3,6,5,3,2,1,4,5]
zw=ste.count(1)
print(zw)
print("are all ok")
re="str","pyt","lis","tup","complex","str","pyt","lis","tup","complex","str","pyt","lis"
de=re.count('str')
print(de)
