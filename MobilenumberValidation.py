import re
cno=int(input("enter a cno:"))
if cno<=12:
    print("It is ok")
else:
     print("enter only 10 digits")
patt=re.compile(r"(91/0)?[7-9][0-9]{9}")
result=patt.match(cno)
if result:
    print("valid contact")
else:
    print("not a valid")