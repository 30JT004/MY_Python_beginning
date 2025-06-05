print("\033[34m","MATH GAME","\033[0m")

multiple=int(input("Enter your multiple:"))

print("Here are your questions!")
print()
count=0
for i in range(1,11):
  ans=int(input(f"{i} * {multiple} : "))
  if ans == i*multiple:
    print("Great!! That's the correct answer!\n")
    count+=1 
  else:
    print("Oops! That's wrong.\n")


print(f"Congractulations! you gave {count} correct answers!!")