Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="shaym"
a="shyam,shu"
print(a)
shyam,shu
s="shyam"
s[0:9]
'shyam'
s[9]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[9]
IndexError: string index out of range
s[0]
's'
s[:3]
'shy'
s[1,9,1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s[1,9,1]
TypeError: string indices must be integers
s[1:9:1]
'hyam'
s[0:9:2]
'sym'
s[-1:-10]
''
[-1:-4]
SyntaxError: invalid syntax
s[-1:-4]
''
s[-4:-1]
'hya'
s[-5:-1:2]
'sy'
s[-4:-1:-1]
''
s[-1:-4:-1]
'may'
s[-4:-1]
'hya'
s[-1:-4]
''
s[::]
'shyam'
s[1::1]
'hyam'
s[-1::-1]
'mayhs'
i=0
for i in range(0,len(s)):
    print(s[i])

    
s
h
y
a
m
while i<len(s):
    print(s[i])
    i++
    
SyntaxError: invalid syntax

y="youtuber"
s+y
'shyamyoutuber'
s*3
'shyamshyamshyam'
3*s
'shyamshyamshyam'
"sh"in s
True
"sh"not in s
False
len(s)
5
s.count()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
s.count("s")
1
y.count("e")
1
s.find("shy")
0
s.find("shyam")
0
s.find("yam")
2
y.find("u"1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
y.find("u",1)
2
s.startswith("shya")
True
s.endswith("shay")
False
s.endswith("yam")
True
s.upper()
'SHYAM'
s.lower()
'shyam'
s.swapcase()
'SHYAM'
s.title()
'Shyam'
s.isupper()
False
s.islower()
True
f="FDJDSH"
f.capitalize()
'Fdjdsh'
s.capitalize()
'Shyam'
s.isalnum()
True
s.isalpha()
True
s.isdigit()
False
s.isspace()
False
s.center(20)
'       shyam        '
s.ljust(20,"-")
'shyam---------------'
s.center(20,"-")
'-------shyam--------'
d=("sai","shyam")
j="loves"
j.join(d)
'sailovesshyam'
s.expandtabs(20)
'shyam'
s.partition("h")
('s', 'h', 'yam')
y.split("u")
['yo', 't', 'ber']
y.split("u",2)
['yo', 't', 'ber']
y.split("u",1)
['yo', 'tuber']
string.whitespace
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    string.whitespace
NameError: name 'string' is not defined
s.whitespace
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.whitespace
AttributeError: 'str' object has no attribute 'whitespace'
s.count("s")
1

=================================================== RESTART: C:/Users/T.SHYAM/Desktop/number of times letter.py ===================================================
enter string:"shyam"
7

=================================================== RESTART: C:/Users/T.SHYAM/Desktop/number of times letter.py ===================================================
enter string:"shaym"
1
