def multisum(x,y):
    return x*y if x*y <= 1000 else x+y

a,b = input("enter two numbers: ").split()

print(multisum(int(a), int(b)))
