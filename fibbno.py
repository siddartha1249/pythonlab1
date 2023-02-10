n=int(input("enter the no of fibnocci digits"))
x=0
y=1
if n == 1 :
    print(x)
elif n == 0 :
    print("nothing")
elif n == 2 :
    print(x,y)
else :
    print(x,y)
    t = n-2
    while t > 0 :
        z=x+y
        print(z)
        x=y
        y=z
        t = t-1
