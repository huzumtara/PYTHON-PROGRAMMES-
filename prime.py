# finding the prime number
n=int(input("enter the number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(f"not prime number")
            break
    else:
        print(f"a prime number")    
else:
    print("out of loop")
