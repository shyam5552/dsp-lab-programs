Python 3.10.4 (tags/v3.10.4:9d38120, May 11 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3,4]
for i in l:
    print(i)

    
1
2
3
4
#adding elements to list
l.extend([5,6,7])
l
[1, 2, 3, 4, 5, 6, 7]
l.extend
<built-in method extend of list object at 0x000001C307F03300>

9
l.extend([1,2,3,[3,4]])
l
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, [3, 4]]
l.append(9)
l
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, [3, 4], 9]
l.append(8,9)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l.append(8,9)
TypeError: list.append() takes exactly one argument (2 given)
l.append((8,9))
l
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, [3, 4], 9, (8, 9)]
l.insert(0,10)
l
[10, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, [3, 4], 9, (8, 9)]
l.remove([8,9])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l.remove([8,9])
ValueError: list.remove(x): x not in list
l.remove(10)
;
SyntaxError: invalid syntax
l
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, [3, 4], 9, (8, 9)]
l.pop(1)
2
l.pop(4)
6
l
[1, 3, 4, 5, 7, 1, 2, 3, [3, 4], 9, (8, 9)]
l.clear()
l
[]
#for deleting all elements
l=[1,2,3,4,5]
del(l[-1])
l
[1, 2, 3, 4]
len(l)
4

#slicing
l
[1, 2, 3, 4]
l[o]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    l[o]
NameError: name 'o' is not defined
l=[1,2,3,4]
l[0]
1
l[1:]
[2, 3, 4]
L[0]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    L[0]
NameError: name 'L' is not defined. Did you mean: 'l'?
l[0]
1
l.sort()
l
[1, 2, 3, 4]
#methods
l
[1, 2, 3, 4]
l.reverse()
l
[4, 3, 2, 1]
