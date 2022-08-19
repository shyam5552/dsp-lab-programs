import re
txt="the rain is comming the r"
x=re.search("is",txt)
x1=re.match("[a-m]",txt)
print(x1)
y=re.findall("mm",txt)
print(x)
print(y)

#+
p=re.findall("th.*r",txt)
p1=re.findall("th.*r",txt)
print(p)
print(p1)
#{}
f=re.findall("t.{3}r",txt)
print(f)
#\b \A  \d \D \w \Z
string="thisskjf"
c=re.match("[a-m]",txt)
print(c)
