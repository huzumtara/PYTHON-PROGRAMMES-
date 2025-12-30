#printing prime number using while loop
n=int(input("enter the number"))
if n>1:
      i=2
      while i<n:
          if n%i==0:
               print(f" not prime")
               break
          i+=1
      else:
          print(f" a prime")
else:
      print("out of the loop")
      

