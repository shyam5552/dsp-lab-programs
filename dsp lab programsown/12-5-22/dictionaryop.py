Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
print(d)
{}
type(d)
<class 'dict'>
d["name"]="shyam"
print(d)
{'name': 'shyam'}
d["rno"]=46
print(d)
{'name': 'shyam', 'rno': 46}
d["rno"]=44
print(d)
{'name': 'shyam', 'rno': 44}
d.keys()
dict_keys(['name', 'rno'])
d.values()
dict_values(['shyam', 44])
d.items()
dict_items([('name', 'shyam'), ('rno', 44)])
d.pop("rno")
44
print(d)
{'name': 'shyam'}
d.popitem()
('name', 'shyam')
print(d)
{}
