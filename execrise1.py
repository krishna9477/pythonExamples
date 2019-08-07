#prime

num=int(input("enter a no:"))
if num>=1:
    for i in range(2,num//2):
        if num%i==0:
            print("not a prime")

    else:
        print("prime number")
else:
    print("Enter +ve only and >1")