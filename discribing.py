#describing a person using both position and keyword arguments in arbritrary 
def des_per(*arg,**kwarg):
    print("position arguments:",arg)
    print(type(arg))
    print("keyword arguments:",kwarg)
    print(type(kwarg))
print(des_per(10000,name="HUZUM",city="hyderabad"))    

