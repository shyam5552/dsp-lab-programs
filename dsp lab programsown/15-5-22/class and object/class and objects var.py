class car:
    wheel=4

    def __init__(self):
        self.mil=10
        self.com='as'
c1= car()
c2=car()
# for changing inatance variable
c1.mil=30

#for changing class variable
car.wheel=7
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)        
