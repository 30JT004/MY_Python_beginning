import random

print("\033[36m","Guess the number One-To-One-Million","\033[0m")
count=0
num=random.randint(1,100000)

print("Lets Start the game!!!")


play_again=""
while play_again != "yes": 
 anss=int(input("What is your guess? "))
 count=count+1

 if (anss==num):
   print(f"""That's Correct!!
         You took {count} guesses to answer correctly! """)
   break
 
 elif (anss>num):
   print("Wrong! That's greater than the number!")
   continue

 else:
   print("Wrong! That's lesser than the number!")
   continue

   break

print(f"You took {count} guesses to answer correctly!")
play_again=input("Do you want to play again?").lower()