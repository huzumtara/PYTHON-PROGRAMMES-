# arbitrary arguments(keyword arguments)
def add_4(**kwargs):
    print("keyword arguments:",kwargs)
    print(type(kwargs))
    
print(add_4(name="HUZUM",age=28,city="hyderabad",salary=1000000))
