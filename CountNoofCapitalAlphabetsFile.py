string=input("enter a string:")
count1=0
count2=0
count3=0
count4=0

rep=string.replace('a','*')
print(rep)

for i in string:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
    elif(i.isdigit()):
        count3+=1
    elif (i.isspace()):
        count4 += 1
print("the lower case letters:",count1)
print("the upper caase letters:",count2)
print("the  digits letters:",count3)
print("the  space letters:",count4)
