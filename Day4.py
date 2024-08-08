# def childerns(*kids):
#     print("Youngest child is :" + kids[1])
# childerns("sunil","bharat","manoj")

# def childrens(child1,child3,child2):
#     print("Name of the Child: ", child2)                                 #key word arguments
# childrens(child1="MANOJ",child2 ="Sunil",child3="bharat")


# def childerns(**kids):
#     print("last name: ",kids["lname"])                        #orbitary keyword arguments
# childerns(fname="MANOJ",lname="n")

# def func(country="India"):
#     print("Country is: ",country)
# func("russia")
# func("germany")                                                    
# func()                                                                        #default arguments2


# x=lambda a,b,c : a+b+c+10
# print(x(5,6,7))

def func(n):
    return lambda a : a*n
double = func(2)
triple = func(6)
print(double(11))
print(triple(22))