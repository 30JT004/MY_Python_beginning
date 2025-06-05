print("GENERATION IDENTIFIER")
print()
year=int(input("What year were you born in?\n"))
print()
if year < 1883 :
  print("Youre too old!")
elif (year<=1990) and (year>=1883):
  print("Lost Generation!")
elif (year<=1927) and (year>=1991):
  print("Greatest Generation!")
elif (year<=1945) and (year>=1928):
  print("Silent Generation!")
elif (year<=1964) and (year>=1946):
  print("Bbaby Boomers!")
elif (year<=1980) and (year>=1965):
  print("Generation X!")
elif (year<=1996) and (year>=1981):
  print("Millenials!")
elif (year<=2012) and (year>=1997):
  print("Generation Z!")
else:
  print("Generation Alpha!")