def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
        else:
            print("prime")
n=int(input("enternum:"))
prime(5)            
            
