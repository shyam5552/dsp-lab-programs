Python 3.10.4 (tags/v3.10.4:9d38120, May 12 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

t=(1,2,3,4)
t
(1, 2, 3, 4)
t.length()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t.length()
AttributeError: 'tuple' object has no attribute 'length'
length(t)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    length(t)
NameError: name 'length' is not defined
length(t)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    length(t)
NameError: name 'length' is not defined
len(t)
4
type(t)
<class 'tuple'>
t.count(1)
1
t.index(0)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    t.index(0)
ValueError: tuple.index(x): x not in tuple
t.index(1)
0
t[1]
2
t[1:4]
(2, 3, 4)
t[-1]
4
t[-1:0]
()
t
(1, 2, 3, 4)
t[:-1]
(1, 2, 3)
t[-1:]
(4,)
t
(1, 2, 3, 4)
list(t)
[1, 2, 3, 4]
tuple(t)
(1, 2, 3, 4)
del(t)
t
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    t
NameError: name 't' is not defined
t=(1,2,3,4)
(a,b,c,d)=t
print(a,b,c,d)
1 2 3 4
for in t:
    
SyntaxError: invalid syntax
for i  in t:
    print(i)

    
1
2
3
4
t1=(6,7,8)
t+t1
(1, 2, 3, 4, 6, 7, 8)
t2=('a','b')
t2*2
('a', 'b', 'a', 'b')
t*2
(1, 2, 3, 4, 1, 2, 3, 4)
