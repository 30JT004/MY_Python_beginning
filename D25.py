import random

print("⚔️ CHARACTER STAT GENERATOR ⚔️")
print()

def dice1(a):
  num1=random.randint(0,a)
  return num1
  
def dice2(b):
  num2=random.randint(0,b)
  return num2

def health_stat():
    char=input("Name your Character : ")
    print(f"{char} health stat : {dice1(6)*dice2(8)}")
    

while True:
  health_stat()

  ans=input("Do you want to stop? ").lower()

  if ans == "yes":
   print("Bye!")
   break
  else:
    continue
 
  break

