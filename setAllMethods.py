s1={1,2,4,3,5,6}
s2={'sweet','hot','sexy',1,2,3,4}
#s1.intersection_update(s2)
#print(s1)

s1.intersection(s2)
print(s1)


print("===========================")

# clear method
l={1,2,4,3,5,6}
l2={'sweet','hot','sexy',1,2,3,4}
print(l2)
l2.clear()
print(l2)

print("===========================")

# add()
p1={1,2,3}
p1.add(4)
print(p1)
print("===========================")

#copy()

h1={1,2,3}
h2={1,68,94}
x=h2.copy()
print(x)
print(h2)

print("===========================")
#difference

k1={1,2,3}
k2={3,4,5}
print(type(k2))
k3=k1.difference(k2)
print(k3)
print("===========================")
#update
i={1,2,3}
i1={3,5,9}
i.update(i1)
print(i)