# arbitrary arguments it can be a name (position)
def add_2(*a):
    print("position arguments:",a)
    print(type(a))
    return sum(a)

print(add_2(10,60,50,90))
  
 



