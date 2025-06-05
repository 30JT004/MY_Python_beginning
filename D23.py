print("REPLIT LOGIN SYSTEM")
print()
username1=input("Enter username : ")
password1=input("Enter password : ")


def login():
 
 print("LOGIN:")
 print()
 while True:
  username=input("Enter username : ")
  password=input("Enter password : ")
  print()
  
  if ((username==username1) and (password==password1)):
    print("Welcome to REPLIT")
    break

  else:
    print("The username or password is incorrect.\n")
    continue 

    break 
  
login()    
