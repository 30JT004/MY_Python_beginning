import random

def roll_dice():

 
 while True:
  
  sides=int(input("How many sides of the dice do you want?\n"))
  choice=random.randint(0,sides)
  print(f"You chose {choice}.")

  play=input("Dou you want to continue playing?")

  if (play=="no"):
   print("Bye!")
   break
  else:
   print()   
   continue

   break 

roll_dice()