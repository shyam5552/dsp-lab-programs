class computer:
    def __init__(self):
        self.name="shyam"
        self.age=20
    def compare(self,c2):
        if c1.age==c2.age:
            return True
        else:
            return False
   
c1=computer()
c2=computer()
c1.age=20
if c1.compare(c2):
    print("")
else:
    print("hjg")
