x=int(input("Enter no.:"))
def Fact(n):
    if n<=1:
        return 1
    else:
        return n*Fact(n-1)
print("Factorial of ",x, " is: ",Fact(x))
