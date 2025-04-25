def gcd(a,b):
    smallest=a if a<b else b
    for i in range(1,smallest):
        if (a%i==0 and b%i==0):
            g=i
    return g

def lcm(a,b):
    greatest=a if a>b else b
    while True:
        if(greatest%a==0 and greatest%b==0):
            l=greatest
            return greatest
        greatest+=1

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
choice=input("Enter either lcm or gcd as your choice:")
if choice=="lcm":
    print("The LCM is: ",lcm(n1,n2))
elif choice=="gcd":
    print("The GCD is: ",gcd(n1,n2))
else:
    print("Invalid choice")


