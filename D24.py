def cake_baking(ingredients,base,coating):
  if ingredients=='chocolate':
    print(f"Wow that a tasteful {ingredients} cake.")
  elif ingredients=='brocolli:':
      print(f"Ew! A brocolli cake???")
  elif ingredients=='carrot':
     print(f"Oh, i guess {ingredients} cake is good!")
  else:
     print("Thats good")
  print(f"You want a {ingredients} cake with {base} base and {coating} topings.")


used_ingredients=input("What is the main Ingredient : ")
used_base=input("what is the base : ")
used_iceing=input("What iceing do you want : ")

cake_baking(used_ingredients,used_base,used_iceing)

