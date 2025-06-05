print("BILLS😩")
i = 1
amt=1000
for i in range (10) :
   amt+=amt*0.05*10
   print(f"Year {i+1}  accounts to {amt}")

print("the profit earned in 10 years is: ",amt-1000)