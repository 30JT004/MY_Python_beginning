print(" Wanna hear some.... Animal Sounds????\n LETS GO!!")

exit=""
while exit != "YES":
 animal=input("Which animal's sound do you want?\n")

 if animal == "COW" :
  print(f"The {animal} goes MOOO.")
 elif animal == "FROG":
  print(f"The {animal} goes CROAK.")
 elif animal == "HORSE":
  print(f"The {animal} goes NEIGH.")
 elif animal == "DOG":
  print(f"The {animal} goes BARK.")
 elif animal == "CAT":
  print(f"The {animal} goes MEOW.")
 elif animal == "DUCK":
  print(f"The {animal} goes QUACK.")
 elif animal == "SNAKE":
  print(f"The {animal} goes HISS.")
 elif animal == "TIGER" or animal == "LION" or animal =="BEAR" :
  print(f"The {animal} goes ROAR.")
 elif animal == "ELEPHANT":
  print(f"The {animal} goes TRUMPET.")
 else:
  print("Sorry! Seems like we dont have the full set of animals😔.")

  exit=input("Want to stop?\n")    