print("ROCK PAPER SCISSORS! 🪨🗞️✂️")
print("""RULES:
R for rock 🪨
P for paper 🗞️
S for scissors ✂️""")

count1=0
count2=0
while True:
  
  P1=input("What do you choose player 1?")
  P2=input("What do you choose player 2?")

  if P1 == P2 :
   print("""GREAT CHEMISTRY.....
           Boht played :""",P1)
   print("Try again")
   continue

  if((P1 == "R" and (P2 == "P" or P2 == "S") ) or (P1 == "S" and P2 == "P" ) or (P1 == "P" and P2 == "R")):
   count1+=1
   if count1<3:
     print(f"""Player 1 chose:{P1}
Player 2 chose:, {P2} 
So, Player 1 WINNNNS🥳!!!""")
   else :
     print(f"Player 1 has won after playing, Scoring {count1} WINS!")
     break

  else:
    count2+=1
    if count2<3:
      print(f"""Player 1 chose: {P1}
Player 2 chose:, {P2}
So, Player 2 WINNNNS🥳!!!""")
    else :
      print(f"Player 2 has won after playing, Scorinf {count2} WINS!")
      break