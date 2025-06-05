print("\033[21m","\033[31m","List Generator","\033[0m","\033[0m")

i=int(input("Enter the lowerbound:\n"))
j=int(input("Enter upperbound:\n"))
j=j+1
inc=int(input("Enter Increment value:\n"))
print(f"Values incremented by {inc} from {i} till {j-1} are:")

for i in range(i,j,inc):
  print(i)