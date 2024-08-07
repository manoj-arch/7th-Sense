username = input("Enter The Name: ")
password= int(input("Enter The password: "))

def validate():
    if(username == "manoj" and password == 7892):
        print("login successfully")
    else:
        print("access error")
validate()