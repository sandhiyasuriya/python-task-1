granted = False
def grant():
    global granted
    granted = True
    if(granted==True):
        print("Congratulations and welcome to gmail account")
        print("### USER DETAILS ###")
        print("Username: ",username)
        
def login(username,password):
    success = False
    for line in open("User_Data.txt","r").readlines(): 
        login_info = line.split() 
        print(login_info)
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            return True
            success = True            
    print("Incorrect credentials.")
    return False
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")

def register(name,password):
    file = open("User_Data.txt","a")
    file.write("\n"+name+","+password)
    grant()

def access(option):
    global name
    if(option==1):
        username = input("Enter your name: ")
        password = input("Enter your password: ")
        login(username,password)
    else:
        print("Enter your name and password to register")
        username = input("Username : ")
        m=username.find('@')+1
        mis_chars=['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*']
        if username[0] not in mis_chars:
            for special in username:
                if(username[m]!='.'):
                    print("Valid Username")
                    l, u, p, d = 0, 0, 0, 0
                    password = input("Password :")
                    if (len(password) > 5 and len(password)<16):
                        for i in password:
                            if (i.islower()):
                                l+=1           
                            if (i.isupper()):
                                u+=1           
                            if (i.isdigit()):
                                d+=1           
                            if(i=='@'or i=='$' or i=='_'):
                                p+=1          
                    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
                        print("Password Validated")
                        f = open("User_Data.txt",'r')
                        info = f.read()
                        if username in info:
                            return "Name Already exist. Please Try Again"
                        else:
                            f = open("User_Data.txt",'a')
                            #info = info+","+username+","+password
                            #L = [username,password]
                            f.write(username)
                            f.write(",")
                            f.write(password)
                            f.write("\n")
                            f.close() 
                            return "You have successfully registered with gmail account!!!"
                        f.close()
                    else:
                        print("Invalid Password")
                else:
                    print("Invalid Username")
                    break
        else:
            print("Invalid Username")
        register(username,password)

def begin():
    global option
    print("welcome to gmail account!!!")
    option = int(input("Login or Signup(for new Registration) \n Type 1 for Login, \n Type 2 for Register: "))
    if(option!=1 and option!=2):
        print("Invalid input provided")
        begin()
    else:
        access(option)        
begin()




        



