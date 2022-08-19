import re
string="6730911492"
c=re.match("[7-9]+[0-9]{9}",string)
if(c):
    print("matched")
else:
    print("not match")



#email id
email="thurubilli2003@gmail.com"
x=re.match("[a-z|A-z]+[0-9]+[@][a-z]+[.][a-z]{3}",email)
if(x):
    print("matched")
else:
    print("not matched")
