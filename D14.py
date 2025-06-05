from getpass import getpass as input
print()
print("""       SHOWDOWNNNNN🔥🔥
      ROCKS🪨 PAPERS🗞️ AND SCISSORS✂️ """)


print("""RULES ⛓️: 
      P for Paper
      R for Rock
      S for scissors
      AND NOW............. GO!!!!!!""")


print("""OH! YES you're safe🦺!!!!
      Your opponent wont be able to see your move !! 🔎😶‍🌫️""")



P1=input("Player 1 chooses:")
print()
P2=input("Player 2 chooses:")
print()



if P1 == P2 :
  print("""GREAT CHEMISTRY.....
           Boht played :""",P1)
  print("Try again")



elif((P1 == "R" and (P2 == "P" or P2 == "S") ) or (P1 == "S" and P2 == "P" ) or (P1 == "P" and P2 == "R")):
  print(f"""Player 1 chose:{P1}
Player 2 chose:, {P2} 
So, Player 1 WINNNNS🥳!!!""")



else:
    print(f"""Player 1 chose:, {P1}
Player 2 chose:, {P2} 
So, Player 2 WINNNNS🥳!!!""") 