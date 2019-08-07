mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(type(myit))


print("==================")
mytuple = ("apple", "banana", "cherry")
if 'apple' in mytuple:
    print("yes")
else:
    print("no")