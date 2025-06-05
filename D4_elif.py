print("""MY LOGIN SYSTEM
      +++++++++++++++++++""")

print()

name=input("Username > ")
pswd=input("Password >")
print()
if name=="David" and pswd =="password":
  print("Why hello there ",name, ", what a lovely accent you have, you could have charmed your way in here even without a password.\n Have a great Day!\nDont forget to wear a hat in the sun!")
elif name=="Sonia" and pswd=="sonia7":
  print("Hey! Sonia its been a long time, weve missed you here, lets get back on business asap!")
else:
  print("Get Out!!!!!!")
