from getpass import getpass as input
import random
print("GUESS THE NUMBER😮😮")

number = random.randint(1,500)

while True:
  no=int(input("""A number has been chosen,
MAKE A GUESS!!!🤔🤔"""))
  if(no==number):
    print("THAT'S CORRECT!!!!!!")
    break
  elif(no>number):
    print("You're thinking Higher.... amke another guess ")
    continue
  elif(no<number):
    print("Youre Thinking Lower..... make another guess")
    continue  
  else:
    print("Wrong Choice")
    continue
  
  break