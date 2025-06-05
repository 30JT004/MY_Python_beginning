print("While true loop")
count=0

while True:
  inputt=int(input("Hello, Enter a number:"))
  count+=inputt
  print("The cumulative sum is:",count)
  stop=input("Do you want to stop?")
  if stop == "YES":
   break

print("OKAY! BYEE")