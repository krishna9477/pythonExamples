l=['a','b','c','d','e','f']
print([l[i-2:i+1] for i in range(2,len(l))])

print("=====================================================================")

a = ['a','b','c','d','e','f']
#print([a[i*3:(i+1)*3] for i in range(len(a)/3)])

#or
print([a[i:i+3] for i in range(0,len(a),3)])